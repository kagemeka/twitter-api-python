from lib.adam import (
  Adam,
)



def main():
  Adam()() 
  # get = GetAuthFrom()
  # auth = get.secrets_manager(
  #   'adam-twitter',
  # )
  # params = Params()
  # make = MakeRequest()
  # request = make(
  #   params=params,
  # )
  # send = SendRequest(auth)
  # res = send(request).json()
  # convert = ConvertTweet()
  # print(res)
  # res = convert(res['data'][0])
  # print(res)



def lambda_handler(
  event,
  context,
):
  main()


if __name__ == '__main__':
  main()