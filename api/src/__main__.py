from lib.adam import (
  Adam,
)


from lib.twitter.tweets import(
  ConvertTweet,
)

from lib.twitter.tweets.sampled_stream import (
  Params,
  MakeRequest,
)

from lib.twitter import (
  GetAuthFrom,
)
from lib.twitter import (
  SendRequest,
)


def main():
  # Adam()() 
  get = GetAuthFrom()
  auth = get.secrets_manager(
    'adam-twitter',
  )
  params = Params()
  make = MakeRequest()
  request = make(
    params=params,
  )
  send = SendRequest(auth)
  res = send(request).json()
  convert = ConvertTweet()
  print(res)
  res = convert(res['data'][0])
  print(res)



def lambda_handler(
  event,
  context,
):
  main()


if __name__ == '__main__':
  main()