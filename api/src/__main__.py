from pprint import (
  pprint,
)


from lib.adam import (
  MakeAdamDF,
  Store,
)




def main():
  df = MakeAdamDF()()
  Store()(df)
  print(df.tweet_cnts)


  


def lambda_handler(
  event,
  context,
):
  main()


if __name__ == '__main__':
  main()