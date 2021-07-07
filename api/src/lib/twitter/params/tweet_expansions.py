import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class ReferencedTweets():
  id: bool = False
  self_: bool = False



@dataclasses.dataclass
class Attachments():
  media_keys: bool = False
  poll_ids: bool = False



@dataclasses.dataclass
class Geo():
  place_id: bool = False



@dataclasses.dataclass
class TweetExpansions():
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