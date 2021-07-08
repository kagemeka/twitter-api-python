import typing
from dataclasses import (
  asdict,
)
import pandas as pd
from .fetch_usernames import (
  FetchUsernames,
)
from \
  lib.twitter.users \
  .user_lookup \
import (
  ByUsernamesParams,
  MakeRequest,
)
from lib.twitter import (
  SendRequest,
)
from lib.twitter.users import (
  ConvertUser,
)
from lib.twitter.auth import (
  GetAuthFrom,
)



class GetUserInfos():
  def __call__(
    self,
  ) -> pd.DataFrame:
    self.__get_usernames()
    self.__set_auth()
    self.__request()
    self.__to_dataframe()
    return self.__df
  

  def __set_auth(
    self,
  ) -> typing.NoReturn:
    get = GetAuthFrom()
    auth = get.secrets_manager(
      'adam-twitter',
    )
    self.__auth = auth
  
  
  def __get_usernames(
    self,
  ) -> typing.NoReturn:
    self.__usernames = (
      FetchUsernames()()
    )

  
  def __request(
    self,
  ) -> typing.NoReturn:
    auth = self.__auth
    send = SendRequest(auth)
    make = MakeRequest()
    names = self.__usernames 
    params = ByUsernamesParams(
      usernames=names,
    )
    f = params.user_fields
    f.public_metrics = True
    req = make.by_usernames(
      params,
    )
    res = send(req).json()
    convert = ConvertUser()
    self.__users = [
      convert(user)
      for user in res['data']
    ]

  
  def __to_dataframe(
    self,
  ) -> typing.NoReturn:
    users = self.__users
    ls = []
    for user in users:
      pm = user.public_metrics
      data = {
        'id': user.id,
        'name': user.name,
        'username': (
          user.username
        ),
        **asdict(pm),
      }
      ls.append(data)
    self.__df = pd.DataFrame(
      ls,
    )