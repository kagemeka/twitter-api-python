import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class Url():
  start: int
  end: int
  url: str
  expanded_url: Optional[
    str
  ] = None
  display_url: Optional[
    str
  ] = None 
  unwound_url: Optional[
    str
  ] = None



@dataclasses.dataclass
class Hashtag():
  start: int
  end: int
  tag: str



@dataclasses.dataclass
class Mention():
  start: int
  end: int
  username: str
  id: str



@dataclasses.dataclass
class Cashtag():
  start: int
  end: int
  tag: str



@dataclasses.dataclass
class Annotation():
  start: int
  end: int
  probability: float
  type: str
  normalized_text: str



@dataclasses.dataclass
class Entities():
  annotations: Optional[
    typing.List[Annotation]
  ] = None
  urls: Optional[
    typing.List[Url]
  ] = None
  hashtags: Optional[
    typing.List[Hashtag]
  ] = None
  mentions: Optional[
    typing.List[Mention]
  ] = None
  cashtags: Optional[
    typing.List[Cashtag]
  ] = None




class ConvertEntities():

  def __call__(
    self,
    data: dict,
  ) -> Entities:
    self.__data = data
    self.__convert()
    return self.__entities
  

  def __convert(
    self,
  ) -> typing.NoReturn:
    self.__entities = Entities(
      **self.__data,
    )
    self.__annotations()
    self.__urls()
    self.__hashtags()
    self.__mentions()
    self.__cashtags()  


  def __annotations(
    self
  ) -> typing.NoReturn:
    entities = self.__entities
    ls = entities.annotations
    if ls is None: return
    entities.annotations = [
      Annotation(**x)
      for x in ls
    ]
  
  def __urls(
    self,
  ) -> typing.NoReturn:
    entities = self.__entities
    urls = entities.urls
    if urls is None: return
    entities.urls = [
      Url(**url)
      for url in urls
    ]
  

  def __hashtags(
    self,
  ) -> typing.NoReturn:
    entities = self.__entities
    tags = entities.hashtags
    if tags is None: return
    entities.hashtags = [
      Hashtag(**tag)
      for tag in tags
    ]
  

  def __mentions(
    self,
  ) -> typing.NoReturn:
    entities = self.__entities
    ls = entities.mentions
    if ls is None: return
    entities.mentions = [
      Mention(**x)
      for x in ls
    ]


  def __cashtags(
    self,
  ) -> typing.NoReturn:
    entities = self.__entities
    ls = entities.cashtags
    if ls is None: return
    entities.cashtags = [
      Cashtag(**x)
      for x in ls
    ]