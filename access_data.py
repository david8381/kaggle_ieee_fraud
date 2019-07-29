import os
import pandas as pd

DATA_DIR = '/home/jovyan/data'
RAW_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')

if not os.path.exists(RAW_DIR):
    os.makedirs(RAW_DIR)

if not os.path.exists(PROCESSED_DIR):
    os.makedirs(PROCESSED_DIR)

def get_raw_sample_submission():
    path = os.path.join(RAW_DIR, 'sample_submission.csv')
    parquet_path = path.replace('.csv', '.parquet')

    if not os.path.exists(parquet_path) or refresh:
        df = pd.read_csv(path)
        df.to_parquet(parquet_path)
    else:
        df = pd.read_parquet(parquet_path)

    return df

def get_identity(train=True, refresh = False):
    path = os.path.join(RAW_DIR, '{}_identity.csv'.format(
        'train' if train else 'test'))
    parquet_path = path.replace('.csv', '.parquet')

    if not os.path.exists(parquet_path) or refresh:
        df = pd.read_csv(path)
        df.to_parquet(parquet_path)
    else:
        df = pd.read_parquet(parquet_path)

    return df

def get_transaction(train=True, refresh=False):
    path = os.path.join(RAW_DIR, '{}_transaction.csv'.format(
        'train' if train else 'test'))
    parquet_path = path.replace('.csv', '.parquet')

    if not os.path.exists(parquet_path) or refresh:
        df = pd.read_csv(path)
        df.to_parquet(parquet_path)
    else:
        df = pd.read_parquet(parquet_path)

    return df

def get_data(train=True, refresh=False):
    path = os.path.join(PROCESSED_DIR, '{}_data.parquet'.format('train' if train else 'test'))
    if not os.path.exists(path) or refresh:
        id_data = get_identity(train, refresh)
        trans_data = get_transaction(train, refresh)
        data = pd.merge(trans_data, id_data,
                how='left', left_on='TransactionID',
                right_on='TransactionID')
        data.to_parquet(path)
    else:
        data = pd.read_parquet(path)
    return data
