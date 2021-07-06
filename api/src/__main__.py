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



def main():
  get = GetAuthOnAWS()
  auth = get.secrets_manager(
    'adam-twitter',
  )
  request = RequestUsers(auth)

  params = {
    'expansions': 'pinned_tweet_id',
    'user.fields': 'public_metrics',
  }
  user = request.by_username(
    username='TwitterDev',
    params=params,
  )

  print(user)




if __name__ == '__main__':
  main()