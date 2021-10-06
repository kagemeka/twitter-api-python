import typing
import boto3
import pandas as pd
from lib.aws_util.s3.download import download_from_s3


def _fetch_keywords() -> typing.List[str]:
  bucket = 'av-adam-store'
  save_path = '/tmp/keyword.csv'
  obj = 'natalie/keyword.csv'
  download_from_s3(bucket, obj, save_path)
  df = pd.read_csv(save_path)
  return df.keyword.unique()