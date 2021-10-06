import typing 
from lib.adam import (
  get_user_infos,
  get_tweet_counts,
  get_tweets,
)


def main() -> typing.NoReturn:
  get_user_infos()
  get_tweet_counts()
  get_tweets()



def lambda_handler(event, context) -> typing.NoReturn:
  get_user_infos()
  get_tweet_counts()
  get_tweets()


if __name__ == '__main__':
  main()