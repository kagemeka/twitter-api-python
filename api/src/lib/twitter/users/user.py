import dataclasses
import typing
from typing import (
  Optional,
)
from datetime import (
  datetime,
)
from .public_metrics import (
  PublicMetrics,
)


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
  location: Optional[
    str
  ] = None
  url: Optional[str] = None
  description: Optional[
    str
  ] = None
  verified: Optional[
    str
  ] = None
  entities: Optional[
    dict
  ] = None
  profile_image_url: Optional[
    str
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