from pprint import (
  pprint,
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

from lib.twitter.tweets import(
  ConvertTweet,
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
  # pprint(params.to_dict())
  make = MakeRequest()
  request = make(params)
  res = send(request).json()
  # pprint(res)
  pprint(
    res['data'][0],
  )
  convert = ConvertTweet()
  tweet = convert(
    res['data'][0],
  )
  print(tweet)

 
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