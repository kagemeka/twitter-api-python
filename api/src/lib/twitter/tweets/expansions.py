import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclsas
class Id():
  self_: bool = False
  author_id: bool = False



@dataclasses.dataclass
class ReferencedTweets():
  id: Optional[Id] = None



@dataclasses.dataclass
class Attachments():
  media_keys: bool = False
  poll_ids: bool = False



@dataclasses.dataclass
class Geo():
  place_id: bool = False



@dataclasses.dataclass
class Expansions():
  author_id: bool = False
  referenced_tweets: Optional[
    ReferencedTweets
  ] = None
  in_reply_to_user_id: bool = (
    False
  )
  attachments: Optional[
    Attachments
  ] = None


  NAME = 'expansions'