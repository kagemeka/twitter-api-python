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
  GetTweets,
)



from lib.twitter.auth import (
  GetAuthFrom,
)

from \
  lib.twitter.tweets \
  .tweet_counts \
import (
  MakeRequest,
  Params,
  ConvertTweetCount,
)

from lib.twitter import (
  SendRequest,
)




def main():
  # get = GetUserInfos()
  # get = GetTweets()
  # users = get()
  # print(users)

  get = GetAuthFrom()
  auth = get.secrets_manager(
    'adam-twitter',
  )
  send = SendRequest(auth)

  params = Params(
    query='twitter',
  )
  make = MakeRequest()
  request = make(params)
  res = send(request).json()
  convert = ConvertTweetCount()
  for data in res['data']:
    data = convert(data)
    print(data)
    
  print(res)


  


 


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