from pprint import (
  pprint,
)


import requests

from datetime import (
  datetime,
  timedelta,
)


from lib.adam import (
  GetUserInfos,
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
  get = GetUserInfos()
  users = get()
  print(users)
  # get = GetAuthFrom()
  # auth = get.secrets_manager(
  #   'adam-twitter',
  # )
  # send = SendRequest(auth)



  # params = Params(
  #   query='twitter',
  # )
  # dt = datetime.now()
  # end = dt - timedelta(
  #   seconds=10,
  # )
  # start = end - timedelta(
  #   days=1,
  # )
  # params.end_time = end
  # params.start_time = start
  # enable = EnableAllParams()
  # enable(params.tweet_fields)
  # enable(params.expansions)
  # enable(params.user_fields)
  # f = params.tweet_fields
  # f.non_public_metrics = False
  # f.organic_metrics = False
  # f.promoted_metrics = False
  # # pprint(params.to_dict())
  # make = MakeRequest()
  # request = make(params)
  # res = send(request).json()
  # # pprint(res)
  # pprint(
  #   res['data'][0],
  # )
  # convert = ConvertTweet()
  # tweet = convert(
  #   res['data'][0],
  # )
  # print(tweet)

 


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