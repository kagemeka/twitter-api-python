import typing 
import sys 



def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/../..')


set_globals()
sys.path.append(f'{root}/src')
from lib.twitter.auth import (
  GetTwitterAuth
)



def test_get_auth_from_secretsmanager() -> typing.NoReturn:
  key = 'adam-twitter'
  auth = GetTwitterAuth.from_secrets_manager(key)
  print(auth)







if __name__ == '__main__':
  test_get_auth_from_secretsmanager()