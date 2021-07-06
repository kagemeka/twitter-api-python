from __future__ import (
  annotations,
)
import typing
import requests
import dataclasses
from typing import (
  Optional,
)
from datetime import (
  datetime,
)
import boto3
import json



  

from lib.twitter.auth import (
  GetAuthOnAWS,
)


from lib.twitter import (
  RequestUsers,
)


import pandas as pd

from pprint import (
  pprint,
)



from lib.twitter.users import (
  UserField,
  Expansion,
)
from lib.twitter.tweets import(
  TweetField,
)

import enum
from enum import (
  auto,
)


from lib.twitter.users import (
  MakeParams,
)



class FetchAnimeUsernames():
  
  def __call__(
    self,
  ) -> typing.List[str]:
    self.__donwload_csv()
    self.__read_csv()
    self.__get_usernames()
    return self.__usernames

  def __get_usernames(
    self,
  ) -> typing.NoReturn:
    df = self.__df
    names = df.twitter_username
    names.dropna(inplace=True)
    names = names.values
    self.__usernames = names
    

  def __read_csv(
    self,
  ) -> typing.NoReturn:
    self.__df = pd.read_csv(
      self.__save_path,
    )
  

  def __donwload_csv(
    self,
  ) -> typing.NoReturn:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(
      'av-adam-entrance',
    )
    ls = bucket.objects.filter(
      Prefix='akibasouken/',
    )
    ls = [o.key for o in ls]
    ls.sort()
    obj = ls[-1]
    self.__save_path = (
      '/tmp/data.csv'
    )
    bucket.Object(
      obj,
    ).download_file(
      self.__save_path,
    )


def main():
  get = GetAuthOnAWS()
  auth = get.secrets_manager(
    'adam-twitter',
  )
  request = RequestUsers(auth)

  user_fields = [
    UserField.ID,
    UserField.USERNAME,
    UserField.NAME,
    UserField.PUBLIC_METRICS,
  ]
  user_fields = [
    field
    for field in UserField
  ]
  expansions = [
    field
    for field in Expansion
  ]
  tweet_fields = [
    field
    for field in TweetField
  ]

  make = MakeParams()
  params = make(
    user_fields=user_fields,   
  )
  

  fetch = FetchAnimeUsernames()
  usernames = fetch()
  users = request.by_usernames(
    usernames=usernames,
    params=params,
  )
  pprint(users[0])
  # s3 = boto3.resource('s3')
  # bucket = s3.Bucket(
  #   'av-adam-entrance',
  # )
  # print(
  #   *bucket.objects.all()
  # )
  



if __name__ == '__main__':
  main()