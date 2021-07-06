import dataclasses
import typing
from typing import (
  Optional,
  List,
)
from datetime import (
  datetime,
)



@dataclasses.dataclass
class Tweet():
  id: str
  text: str
  created_at: Optional[
    datetime
  ] = None
  author_id: Optional[
    str
  ] = None
  conversation_id: Optional[
    str
  ] = None
  in_reply_to_user_id: (
    Optional[str]
  ) = None
  referenced_tweets: Optional[
    List[str]
   ] = None
  attachments: Optional[
    dict
  ] = None
  geo: Optional[
    dict
  ] = None
  context_annotations: (
    Optional[List[dict]]
  ) = None
  entities: Optional[
    dict
  ] = None
  withheld: Optional[
    dict
  ] = None
  public_metrics: Optional[
    dict
  ] = None
  non_public_metrics: Optional[
    dict
  ] = None
  organic_metrics: Optional[
    dict
  ] = None 
  promoted_metrics: Optional[
    dict
  ] = None
  possibly_sensitive: Optional[
    bool
  ] = None
  lang: Optional[str] = None
  reply_settings: Optional[
    str
  ] = None
  source: Optional[str] = None



class ParseTweet():
  def __call__(
    self,
    data: dict,
  ) -> Tweet:
    self.__data = data
    self.__parse()
    return self.__user
  

  def __parse(
    self,
  ) -> typing.NoReturn:
    user = Tweet(**self.__data)
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