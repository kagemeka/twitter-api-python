import typing
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
from . import (
  FetchAnimeUsernames,
)



class GetUserInfos():
  def __call__(
    self,
  ) -> typing.NoReturn:
    self.__get_usernames()
    self.__set_auth()
    self.__request()
    return self.__users

  

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



