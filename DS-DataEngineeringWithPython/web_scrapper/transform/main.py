import argparse
import logging
import hashlib
import glob
logging.basicConfig(level=logging.INFO)
import pandas as pd
from  urllib.parse import urlparse
import nltk
from nltk.corpus import stopwords
# install and download libraries
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('spanish'))

logger= logging.getLogger(__name__)

def main(filename):
    logger.info('Starting cleaning process')
    logger.info(f'Reading...{filename}')
    df = _read_data(filename)
    newspaper_id = _extract_newspaper_id(filename)
    df = _add_newspaper_uid_column(df,newspaper_id)
    df = _extract_host(df)
    df = _fill_missing_titles(df)
    df = _missing_titles(df)
    df = _parse_body(df)
    df['n_tokens_'+ 'title'] = _tokenize_cols(df,'title')
    df['n_tokens_'+ 'body'] = _tokenize_cols(df,'body')
    df = _drop_duplicates(df,'title')
    df = _drop_rows_with_missing_values(df)
    _save_data(df,filename)
    return df


def _save_data(df,file_name):
    new_file_name= 'clean_' + file_name
    logger.info(f'saving file to {new_file_name}')
    df.to_csv(new_file_name)


def _drop_rows_with_missing_values(df):
    logger.info('Removing missing data...')
    return df.dropna()

def _tokenize_cols(df,   col_name):
    return (
        df
        .dropna()
        .apply(lambda row: nltk.word_tokenize(row[col_name]),axis=1)
        .apply(lambda tokens: list(filter(lambda token: token.isalpha(),tokens)))
        .apply(lambda tokens: list(map(lambda token: token.lower(),tokens)))
        .apply(lambda word_list: list(filter(lambda word: word not in stop_words,word_list)))
        .apply(lambda valid_word_list:len(valid_word_list))
    )

def _drop_duplicates(df,col_name):
    logger.info('Removing duplicates...')
    return df.drop_duplicates(subset=[col_name],keep='first')

def _fill_missing_titles(df):
    logger.info('Generating uids for each row...')
    uids = (
        df.apply(lambda row: hashlib.md5(bytes(row['url'].encode())),axis=1)
        .apply(lambda hash_object: hash_object.hexdigest())
    )
    df['uid'] = uids
    df.set_index('uid',inplace=True)
    return df

def _parse_body(df):
    stripped_body =(df 
    .apply(lambda row: row['body'],axis=1)
    .apply(lambda body: list(body))
    .apply(lambda letters: list( map(lambda letter: letter.replace('\n',''),letters) ))
    .apply(lambda letters: list( map(lambda letter: letter.replace('\r',''),letters) ))
    .apply(lambda letters: ''.join(letters))

    )
    df['body']=stripped_body
    return df

def _read_data(filename):
    logger.info(f'Reading file {filename}')
    return pd.read_csv(filename)

def _extract_newspaper_id(filename):
    ## Specific namebase rule
    newspaper_uid = filename.split('_')[0]
    logger.info(f'Newspaper uid detected...{newspaper_uid}')
    return newspaper_uid

def _add_newspaper_uid_column(df,newspaper_uid):
    logger.info(f'Newspaper uid detected {newspaper_uid}')
    df['newspaper_uid'] = newspaper_uid
    return df

def _extract_host(df):
    logger.info('Extracting host...')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)
    return df

def _missing_titles(df):
    missing_titles = (df['url']
    .str.extract(r'(?P<missing_titles>[^/]+)$')
    .applymap(lambda title: title.split('-'))
    .applymap(lambda title_word_list:' '.join(title_word_list))
    )
    df['parsed_titles'] = missing_titles
    return df


if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('profilename',help="Profile to be transformed [file pattern prefix]",type=str)
    arg = parser.parse_args()
    profilename = arg.profilename
    logger.info(f'Processing transformation process for profile {profilename}')
    files = glob.glob(f'{profilename}*.csv')
    for file in files:
        logger.info(f'Starting transformationp process for file {file}')
        df = main(file)
        #print(df)

