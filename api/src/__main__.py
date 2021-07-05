from __future__ import (
  annotations,
)
import typing
import requests
import dataclasses
from typing import (
  Optional,
)
from datetime import (
  datetime,
)
import boto3
import json





@dataclasses.dataclass
class PublicMetrics():
  followers_count: int
  following_count: int
  tweet_count: int
  listed_count: int



@dataclasses.dataclass
class User():
  id: str
  name: str
  username: str
  created_at: Optional[
    datetime
  ] = None
  protected: Optional[
    bool
  ] = None
  withheld: Optional[
    dict
  ] = None
  public_metrics: Optional[
    PublicMetrics
  ] = None
  pinned_tweet_id: Optional[
    str
  ] = None



class ParseUser():
  def __call__(
    self,
    data: dict,
  ) -> User:
    self.__data = data
    self.__parse()
    return self.__user
  

  def __parse(
    self,
  ) -> typing.NoReturn:
    user = User(**self.__data)
    self.__user = user
    self.__public_metrics()
  

  def __public_metrics(
    self,
  ) -> typing.NoReturn:
    user = self.__user
    if not user.public_metrics:
      return
    pm = PublicMetrics(
      **user.public_metrics,
    )
    user.public_metrics = pm



@dataclasses.dataclass
class Tweet():
  id: str
  text: str
  ...



@dataclasses.dataclass
class Includes():
  tweets: typing.List[Tweet]


class ParseIncludes():
  def __call__(
    self,
    data: dict,
  ) -> Includes:
    self.__data = data
    self.__parse()
    return self.__includes
  

  def __parse(
    self,
  ) -> typing.NoReturn:
    includes = Includes(
      **self.__data,
    )
    self.__includes = includes
    self.__tweets()


  def __tweets(
    self,
  ) -> typing.NoReturn:
    includes = self.__includes
    if includes.tweets is None:
      return
    includes.tweets = [
      Tweet(**tw)
      for tw in includes.tweets
    ] 
     


@dataclasses.dataclass
class Response:
  data: User
  includes: Optional[
    Includes
  ] = None
  errors: Optional[
    dict # TODO change later
  ] = None



class ParseResponse():
  
  def __call__(
    self,
    response: (
      requests.models.Response
    ), 
  ) -> Response:
    self.__res = response
    self.__parse()
    return self.__res
  

  def __parse(
    self,
  ) -> typing.NoReturn:
    self.__res = Response(
      **self.__res.json(),
    )
    self.__data()
    self.__includes()
    self.__errors()
  
  
  def __data(
    self,
  ) -> typing.NoReturn:
    res = self.__res
    if res.data is None:
      return
    res.data = ParseUser()(
      res.data,
    )
  
  def __includes(
    self,
  ) -> typing.NoReturn:
    res = self.__res
    if res.includes is None:
      return
    parse = ParseIncludes()
    res.includes = parse(
      res.includes,
    )
  

  def __errors(
    self,
  ) -> typing.NoReturn:
    ... 
    
    
  

from lib.twitter.auth import (
  GetAuthOnAWS,
)




def main():
  get = GetAuthOnAWS()
  auth = get.secrets_manager(
    'adam-twitter',
  )
  token = (
    'Bearer '
    f'{auth.bearer_token}'
  )
  url = (
    'https://api.twitter.com/2/users/by/username/TwitterDev'
  )

  params = {
    'expansions': 'pinned_tweet_id',
    'user.fields': 'public_metrics',
  }
  res = requests.get(
    url=url,
    headers={
      'Authorization': token,
    },
    params=params,
  )
  res = ParseResponse()(res)
  print(res)


  
  '''TODO
  anyway, it's possible that data does not exist.
  '''
  


if __name__ == '__main__':
  main()