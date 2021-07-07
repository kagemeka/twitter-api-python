import typing
from dataclasses import (
  asdict,
)
import pandas as pd
from lib.twitter.auth import (
  GetAuthOnAWS,
)
from lib.twitter import (
  RequestUsers,
)
from lib.twitter.users import (
  UserField,
  MakeParams,
)
from lib.twitter.users.expansions import Expansion
from . import (
  FetchAnimeUsernames,
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
    get = GetAuthOnAWS() 
    auth = get.secrets_manager(
      'adam-twitter',
    )
    self.__auth = auth
  
  
  def __get_usernames(
    self,
  ) -> typing.NoReturn:
    self.__usernames = (
      FetchAnimeUsernames()()
    )

  
  def __request(
    self,
  ) -> typing.NoReturn:
    auth = self.__auth
    f = RequestUsers(auth)
    user_fields = [
      UserField.PUBLIC_METRICS,
    ]
    params = MakeParams()(
      user_fields=user_fields,
    )
    names = self.__usernames
    users = f.by_usernames(
      usernames=names,
      params=params,
    )
    self.__users = users

  
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
        'username': user.username,
        **asdict(pm),
      }
      ls.append(data)
    self.__df = pd.DataFrame(
      ls,
    )