import typing 
import sys 



def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/..')


set_globals()
sys.path.append(f'{root}/src')
from lib.adam import (
  get_user_infos,
  get_tweet_counts,
  get_tweets,
)


def test_get_users() -> typing.NoReturn:
  get_user_infos()


def test_get_tweets() -> typing.NoReturn:
  get_tweets()



def test_get_tweet_cnts() -> typing.NoReturn:
  get_tweet_counts()



if __name__ == '__main__':
  # test_get_users()
  # test_get_tweets()
  test_get_tweet_cnts()
