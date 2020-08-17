import logging
logging.basicConfig(level=logging.INFO)
import subprocess
import os

logger = logging.getLogger(__name__)

news_sites_uids = ['eluniversal','elpais']

# if having a virtual environment configured then specify the path here:
_python_exe = '''C:\Python\envs\prime\Scripts\python.exe'''
_cwd = os.getcwd()

def main():
    logging.info('Beginning ETL  Process...')
    _extract()
    _transform()
    _load()
    logging.info('ETL Process Done!')


def _extract():
    logging.info('Starting extracting process...')
    for news_site_uid in news_sites_uids:
        subprocess.run([_python_exe,'main.py',news_site_uid],cwd=f'{_cwd}\\extract')
        cmdline =f"move /Y {news_site_uid}* ..\\transform"
        logging.info(f'Executing command [{cmdline}]...')
        subprocess.run(cmdline,cwd='.\\extract',shell=True)
    logging.info('Extract finished!')

def _transform():
    logging.info('Starting transform process...')
    for news_site_uid in news_sites_uids:
        dirty_data_filename = f'{news_site_uid}*.csv'
        clean_data_filename = f'clean_{news_site_uid}*.csv'
        subprocess.run([_python_exe,'main.py',news_site_uid],cwd=f'{_cwd}\\transform')
        subprocess.run(['move','/Y',clean_data_filename,'..\\load'],cwd='.\\transform',shell=True)
        subprocess.run(['del', '/F',dirty_data_filename],cwd='.\\transform',shell=True)
    logging.info('Transform finished!')
        


def _load():
    logging.info('Starting load process...')
    for news_site_uid in news_sites_uids:
        subprocess.run([_python_exe,'main.py',news_site_uid],cwd=f'{_cwd}.\\load')
        subprocess.run(['del', '/F',f'*{news_site_uid}*.csv'],cwd='.\\load',shell=True)
    logging.info('Load finished!')

if __name__ == '__main__':
    main()
    