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
class Urls():
  start: int
  end: int
  url: str
  expanded_url: str
  display_url: str



@dataclasses.dataclass
class Url():
  urls: typing.List[Urls]



class ParseUrl():
  def __call__(
    self,
    data: dict,
  ) -> Url:
    self.__url = Url(**data)
    self.__urls()
    return self.__url
  

  def __urls(
    self,
  ) -> typing.NoReturn:
    url = self.__url
    url.urls = [
      Urls(**urls)
      for urls in url.urls
    ]
      


@dataclasses.dataclass
class Hashtag():
  start: int
  end: int
  tag: str



@dataclasses.dataclass
class Description():
  urls: Optional[
    typing.List[Urls]
  ] = None
  hashtags: Optional[
    typing.List[Hashtag]
  ] = None



class ParseDescription():
  def __call__(
    self,
    data: dict,
  ) -> Description:
    self.__d = Description(
      **data,
    )
    self.__urls()
    self.__hashtags()
    return self.__d
  

  def __urls(
    self,
  ) -> typing.NoReturn:
    d = self.__d
    if d.urls is None: return
    d.urls = [
      Urls(**urls)
      for urls in d.urls
    ]
  

  def __hashtags(
    self,
  ) -> typing.NoReturn:
    d = self.__d
    if d.hashtags is None:
      return
    d.hashtags = [
      Hashtag(**tag)
      for tag in d.hashtags
    ]



@dataclasses.dataclass
class Entities():
  url: Optional[Url] = None
  description: Optional[
    dict
  ] = None



class ParseEntities():
  def __call__(
    self,
    data: dict,
  ) -> Entities:
    self.__e = Entities(**data)
    self.__url()
    self.__description()
    return self.__e
  

  def __url(
    self,
  ) -> typing.NoReturn:
    e = self.__e
    if e.url is None: return
    e.url = ParseUrl()(e.url)


  def __description(
    self,
  ) -> typing.NoReturn:
    e = self.__e
    if e.description is None:
      return
    parse = ParseDescription()
    e.description = parse(
      e.description,
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
    Entities
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




from lib import (
  DatetimeFromStr,
)





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
    self.__created_at()
    self.__entities()
  

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
  

  def __created_at(
    self,
  ) -> typing.NoReturn:
    user = self.__user
    dt = user.created_at
    if not dt: return
    dt_from = DatetimeFromStr()
    dt = dt_from.utc_format(dt)

    user.created_at = dt
  

  def __entities(
    self,
  ) -> typing.NoReturn:
    user = self.__user
    e = user.entities
    if e is None: return
    parse = ParseEntities()
    user.entities = parse(e)

