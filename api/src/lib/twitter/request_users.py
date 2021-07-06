import typing
import requests
from .users import (
  User,
  ParseUser,
)

from .auth import (
  TwitterAuth,
)



class RequestUsers():

  def by_id(
    self,
    id_: str,
  ) -> User:
    ... 


  def by_ids(
    self,
    ids: typing.List[str],
  ) -> typing.List[User]:
    ... 


  def by_username(
    self,
    username: str,
    params: dict,
  ) -> User:
    self.__url = (
      'https://api.twitter.com'
      '/2/users/by/username/'
      f'{username}'
    )
    self.__params = params
    self.__request()
    res = self.__response
    return ParseUser()(
      res.json()['data'],
    )
  

  def by_usernames(
    self,
    usernames: typing.List[
      str
    ],
    params: dict,
  ) -> typing.List[User]:
    self.__url = (
      'https://api.twitter.com'
      '/2/users/by'
    )
    s = ','.join(usernames)
    params['usernames'] = s
    self.__params = params
    self.__request()
    res = self.__response
    data = res.json()['data']
    return [
      ParseUser()(user)
      for user in data
    ]


  def __init__(
    self,
    auth: TwitterAuth,
  ) -> typing.NoReturn:
    token = (
      'Bearer '
      f'{auth.bearer_token}'
    )
    self.__headers = {
      'Authorization': token,
    }
  

  def __request(
    self,
  ) -> typing.NoReturn:
    res = requests.get(
      url=self.__url,
      headers=self.__headers,
      params=self.__params,
    )
    self.__response = res
