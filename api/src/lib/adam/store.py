import typing
from datetime import (
  datetime,
)
import boto3
from .make_df import (
  AdamDF,
)



class Store():
  def __call__(
    self,
    df: AdamDF,
  ) -> typing.NoReturn:
    self.__df = df
    self.__add_timestamp()
    self.__save()
    self.__upload()


  def __init__(
    self,
  ) -> typing.NoReturn:
    dt = datetime.now()
    self.__dt = dt
    date = dt.date()
    self.__save_dir = '/tmp/'
    self.__upload_dir = (
      f'twitter/{date}/'
    )

  
  def __add_timestamp(
    self,
  ) -> typing.NoReturn:
    df = self.__df
    dt = self.__dt
    df.tweets['datetime'] = dt
    df.tweet_cnts[
      'datetimee'
    ] = dt
    df.users['datetime'] = dt
  

  def __save(
    self,
  ) -> typing.NoReturn:
    d = self.__save_dir
    tweet_cnts_path = (
      f'{d}tweet_cnts.csv'
    )
    tweets_path = (
      f'{d}tweets.csv'
    )
    users_path = (
      f'{d}users.csv'
    )
    df = self.__df
    df.tweets.to_csv(
      tweets_path,
      index=False,
    )
    df.tweet_cnts.to_csv(
      tweet_cnts_path,
      index=False,
    )
    df.users.to_csv(
      users_path,
      index=False,
    )
    (
      self.__tweet_cnts_path,
      self.__tweets_path,
      self.__users_path,
    ) = (
      tweet_cnts_path,
      tweets_path,
      users_path,
    )
  
    

  def __upload(
    self,
  ) -> typing.NoReturn:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(
      'av-adam-entrance',
    )
    d = self.__upload_dir
    bucket.Object(
      f'{d}tweet_cnts.csv',
    ).upload_file(
      self.__tweet_cnts_path,
    )
    bucket.Object(
      f'{d}tweets.csv',
    ).upload_file(
      self.__tweets_path,
    )
    bucket.Object(
      f'{d}users.csv',
    ).upload_file(
      self.__users_path,
    )
  