#!/usr/bin/env python3

import awswrangler as wr
import pandas as pd
import os
from datetime import datetime
from logging import Logger


# set logger (this will write to CloudWatch)
logger = Logger('root')

# get bucket. you can hardcode it as well
bucket_name = os.getenv('BUCKET')
bucket = f's3://{bucket_name}/dataset'

# here, do what you must to retrive your data, returning a pandas DataFrame
def get_data():
    '''
    Your docstrings
    '''
    return pd.DataFrame(
        {'x': [1,2,3],
        'y': ['a','b','c']}
    )

# attempt to load into S3
try:
    wr.s3.to_parquet(
        df=get_data(),
        path=f's3://{bucket_name}/dataset',
        dataset=True,
        database='database_name',
        table='table_name'
        # optional: Data Catalog Metadata
        # description='The description of database.',
        # parameters={'some_key': 'some_value},
        # columns_comments={'x': 'variable x', 'y': 'variable y'}
    )
    logger.info(f'At {datetime.now().isoformat()}: data insert succesful')

except ConnectionError:
    logger.error(f'At {datetime.now().isoformat()}: data insert failed')
