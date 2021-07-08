import dataclasses
import typing
from typing import (
  Optional,
  List,
)
from datetime import (
  datetime,
)
from .public_metrics import (
  PublicMetrics,
)
from .entities import (
  ConvertEntities,
  Entities,
)
from .context_annotation \
import (
  ConvertContextAnnotation,
  ContextAnnotation,
)


@dataclasses.dataclass
class Tweet():
  id: str
  text: str
  attachments: Optional[
    dict
  ] = None
  author_id: Optional[
    str
  ] = None
  context_annotations: (
    Optional[List[
      ContextAnnotation
    ]]
  ) = None
  conversation_id: Optional[
    str
  ] = None
  created_at: Optional[
    datetime
  ] = None
  entities: Optional[
    Entities
  ] = None
  geo: Optional[
    dict
  ] = None
  in_reply_to_user_id: (
    Optional[str]
  ) = None
  lang: Optional[str] = None
  possibly_sensitive: Optional[
    bool
  ] = None
  public_metrics: Optional[
    PublicMetrics
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
  referenced_tweets: Optional[
    List[str]
  ] = None
  reply_settings: Optional[
    str
  ] = None
  source: Optional[str] = None
  withheld: Optional[
    dict
  ] = None



class ConvertTweet():
  def __call__(
    self,
    data: dict,
  ) -> Tweet:
    self.__data = data
    self.__convert()
    return self.__tweet
  

  def __convert(
    self,
  ) -> typing.NoReturn:
    tweet = Tweet(
      **self.__data,
    )
    self.__tweet = tweet
    self.__public_metrics()
    self.__entities()
    self.__context_annotations()
  

  def __public_metrics(
    self,
  ) -> typing.NoReturn:
    tweet = self.__tweet
    pm = tweet.public_metrics
    if pm is None: return
    pm = PublicMetrics(**pm)
    tweet.public_metrics = pm
  

  def __entities(
    self,
  ) -> typing.NoReturn:
    tweet = self.__tweet
    ent = tweet.entities
    if ent is None: return
    f = ConvertEntities()
    tweet.entities = f(ent)
  

  def __context_annotations(
    self,
  ) -> typing.NoReturn:
    tweet = self.__tweet
    ls = (
      tweet
      .context_annotations
    )
    if ls is None: return
    f = ConvertContextAnnotation()
    (
      tweet
      .context_annotations
    ) = [
      f(annot)
      for annot in ls
    ]
    