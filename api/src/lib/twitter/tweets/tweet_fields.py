import enum
from enum import (
  auto,
)



class TweetField(
  enum.Enum,
):
  ATTACHMENTS = auto()
  AUTHOR_ID = auto()
  CONTEXT_ANNOTATION = auto()
  CONVERSATION_ID = auto()
  CREATED_AT = auto()
  ENTITIES = auto()
  GEO = auto()
  ID = auto()
  IN_REPLAY_TO_USER_ID = auto()
  LANG = auto()
  NON_PUBLIC_METRICS = auto()
  PUBLIC_METRIS = auto()
  ORGANIC_METRICS = auto()
  PROMOTED_METRICS = auto()
  POSSIBLY_SENSITIVE = auto()
  REFERENCED_TWEETS = auto()
  REPLY_SETTINGS = auto()
  SOURCE = auto()
  TEXT = auto()
  WITHHELD = auto()