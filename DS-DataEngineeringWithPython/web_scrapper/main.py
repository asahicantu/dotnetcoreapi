import argparse
import logging
import csv
import datetime
import news_page_objects as news
import re
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

logging.basicConfig(level=logging.INFO)
from common import config

logger = logging.getLogger(__name__)
is_well_formed_link = re.compile(r'^https?://.+/.+$') #i.e https://google.com
is_root_path = re.compile(r'^/.+$') #i.e /sometext

def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']
    logging.info(f'Starting Scrapper for {host}...')
    articles = []

    homepage = news.HomePage(news_site_uid, host)
    for link in homepage.article_links:
        fetch_link = build_link(host,link)
        article = _fetch_article(news_site_uid,host,fetch_link)
        if article:
            articles.append(article)
            logger.info(f'Getting {fetch_link} [{article.title}]')
    logger.info(f'{len(articles)} articles were fetched!...')
    logger.info(f'Writing data...')
    _save_articles(news_site_uid,articles)

def _save_articles(news_site_uid, articles):
    now  = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = f'{news_site_uid}_{now}_articles.csv'
    csv_headers = list(filter(lambda property : not property.startswith('_'),dir(articles[0])))
    with open(out_file_name,'w+') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            try:
                row = [str(getattr(article,prop)) for prop in csv_headers]
                writer.writerow(row)
            except:
                logger.warning(f'Unknown Error while writing article row {article}',exc_info=True)
    logger.info(f'Finished Writing data to file {out_file_name}')

def _fetch_article(news_site_uid, host, link):
    logger.info(f'Fetching article {link}...')
    article = None
    try:
        article = news.ArticlePage(news_site_uid, link)
    except(HTTPError, MaxRetryError) as e:
        logger.warning(f'Error while fetching article {link}',exc_info=False)
    except:
        logger.warning(f'Unknown Error while fetching article {link}',exc_info=True)

    if article  and not article.body:
        logger.warn('Invalid article. No body present')
        return None

    return article

def build_link(host, link):
    if is_well_formed_link.match(link):
        return link
    elif is_root_path:
        return f'{host}{link}'
    else:
        return f'{host}/{link}'

if __name__ == '__main__':
    config_file_name = 'config.yaml'
    news_choices = list(config()['news_sites'].keys())
    parser = argparse.ArgumentParser()

    # parser.add_argument('config_file',
    #                     help="Type config file you want to use",
    #                     type=str,
    #                     default='config.yaml'
    #                     )

    parser.add_argument('news_site',
                        help="Type the url of news site to scrape",
                        type=str,
                        choices=news_choices)
    args = parser.parse_args()

    _news_scraper(args.news_site)