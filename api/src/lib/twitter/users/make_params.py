import typing
import enum
from . import (
  UserField,
  Expansion,
)
from ..tweets import (
  TweetField,
)



class MakeParams():
  def __call__(
    self,
    expansions: typing.List[
      Expansion
    ] = [],
    tweet_fields: typing.List[
      TweetField
    ] = [],
    user_fields: typing.List[
      UserField
    ] = [],
  ) -> dict:
    (
      self.__expansions,
      self.__tweet_fields,
      self.__user_fields,
    ) = (
      expansions,
      tweet_fields,
      user_fields,
    )
    self.__make()
    return self.__params


  def __make(
    self,
  ) -> typing.NoReturn:
    ls = (
      self.__expansions,
      self.__tweet_fields,
      self.__user_fields,
    )
    keys = (
      'expansions',
      'tweet.fields',
      'user.fields',
    )
    self.__params = dict(zip(
      keys,
      map(self.__to_str, ls),
    ))
    

  def __to_str(
    self,
    fields: typing.List[
      enum.Enum
    ],
  ) -> str:
    fields = [
      field.name.lower()
      for field in fields
    ]
    return ','.join(fields)
    