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


from lib.adam import (
  FetchAnimeUsernames,
)



from dataclasses import (
  asdict,
  fields,
)



def main():
  get = GetAuthOnAWS()
  auth = get.secrets_manager(
    'adam-twitter',
  )
  auth.bearer_token = 'AAAAAAAAAAAAAAAAAAAAAE5fRQEAAAAA3Nwl2V78Zu37SgutzF%2BsGHOXoVM%3DA9wydIOtKeo9nrSrzd47pglLEl5Tz32qQbgs4qB4sPqoN3NbeI'
  request = RequestUsers(auth)


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
    expansions=expansions,
    tweet_fields=tweet_fields,  
  )

  fetch = FetchAnimeUsernames()
  usernames = fetch()
  users = request.by_usernames(
    usernames=usernames[:2],
    params=params,
  )
  pprint(users)

  # s3 = boto3.resource('s3')
  # bucket = s3.Bucket(
  #   'av-adam-entrance',
  # )
  # print(
  #   *bucket.objects.all()
  # )
  



if __name__ == '__main__':
  main()