from pprint import (
  pprint,
)



# from lib.adam import (
#   GetUserInfos,
# )


import typing
import boto3
import pandas as pd

from lib.twitter.users.convert_user import public_metrics


class FetchComicKeywords():
  def __call__(
    self,
  ) -> typing.List[str]:
    self.__donwload_csv()
    self.__read_csv()
    self.__get_keywords()
    return self.__keywords
  

  def __get_keywords(
    self,
  ) -> typing.NoReturn:
    df = self.__df
    words = df.keyword.values
    self.__keywords = words
    

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
      Prefix='natalie/',
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




import requests

from datetime import (
  datetime,
  timedelta,
)


# from lib.twitter.params import(

from \
  lib.twitter.users \
  .user_lookup \
import (
  ByUsernamesParams,
  MakeRequest,
)
from lib.twitter.users import (
  ConvertUser,
)

from lib.twitter import (
  SendRequest,
  EnableAllParams,
)

from lib.twitter.auth import (
  GetAuthFrom,
)


from \
  lib.twitter.tweets \
  .search_tweets \
import (
  MakeRequest,
  Params,
)


def main():
  get = GetAuthFrom()
  auth = get.secrets_manager(
    'adam-twitter',
  )
  send = SendRequest(auth)


  # make = MakeRequest()
  # params = ByUsernamesParams(
  #   usernames=['TwitterDev'],
  # )
  # f = params.user_fields
  # f.public_metrics = Truez
  # request = make.by_usernames(
  #   params,
  # )
  # res = send(request).json()
  # convert = ConvertUser()
  # user = convert(
  #   res['data'][0],
  # )
  # print(user)


  params = Params(
    query='twitter',
  )
  dt = datetime.now()
  end = dt - timedelta(
    seconds=10,
  )
  start = end - timedelta(
    days=1,
  )
  params.end_time = end
  params.start_time = start
  enable = EnableAllParams()
  enable(params.tweet_fields)
  enable(params.expansions)
  enable(params.user_fields)
  f = params.tweet_fields
  f.non_public_metrics = False
  f.organic_metrics = False
  f.promoted_metrics = False
  pprint(params.to_dict())
  make = MakeRequest()
  request = make(params)
  res = send(request).json()
  pprint(res)



  # get = GetUserInfos()
  # users = get()
  
  # # pprint(users)

  # fetch = FetchComicKeywords()
  # words = fetch()
  # pprint(words)
  # print(words.size)
  # get = GetAuthOnAWS()
  # auth = get.secrets_manager(
  #   'adam-twitter',
  # )
  # token = (
  #   'Bearer '
  #   f'{auth.bearer_token}'
  # )
  # headers = {
  #   'Authorization': token,
  # }
  # url = (
  #   'https://api.twitter.com/'
  #   '2/tweets/counts/recent'
  # )
  # end = datetime.now()
  # end -= timedelta(seconds=10)
  # start = end - timedelta(
  #   days=1,
  # )
  # # print(start)
  # print(start.isoformat())
  # start = start.isoformat() + 'Z'
  # print(start)
  # end = end.isoformat() + 'Z'


  # print(auth)






  # s3 = boto3.resource('s3')
  # bucket = s3.Bucket(
  #   'av-adam-entrance',
  # )
  # print(
  #   *bucket.objects.all()
  # )
  


def lambda_handler(
  event,
  context,
):
  main()


if __name__ == '__main__':
  main()