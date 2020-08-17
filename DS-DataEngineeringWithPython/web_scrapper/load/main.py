import argparse
import logging
import glob

import pandas as pd
from article import Article
from base import Base, Engine, Session


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(filename):
    Base.metadata.create_all(Engine)
    session = Session()
    articles = pd.read_csv(filename)

    for index,row in articles.iterrows():
        logger.info(f"Loading article uid {row['uid']} into DB...")
        article = Article(row['uid'],
                            row['body'],
                            row['host'],
                            row['newspaper_uid'],
                            row['n_tokens_body'],
                            row['n_tokens_title'],
                            row['title'],
                            row['url']


                            
        )
        session.add(article)
    session.commit()
    session.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('profilename',help="Profile to be transformed [file pattern prefix]",type=str)
    arg = parser.parse_args()
    profilename = arg.profilename
    logger.info(f'Processing loading process for profile {profilename}')
    files = glob.glob(f'{profilename}*.csv')
    for file in files:
        logger.info(f'Starting loading process for file {file}')
        main(file)


    
    
