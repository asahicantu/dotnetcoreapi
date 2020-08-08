import argparse
import logging
logging.basicConfig(level=logging.INFO)
import pandas as pd
from  urllib.parse import urlparse



def main(filename):
    logging.info('Reading...')
    df = _read_data(filename)
    newspaper_id = _extract_newspaper_id(filename)

def _extract_newspaper_id(filename):
    newspaper_uid = filename.split('_')[0]
    return newspaper_uid

def _Read_data(filename):
    return pd.read_csv(filename)

if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',help="Path to the dirty data",type=str)
    arg = parser.parse_args()
    main(arg.filename)
