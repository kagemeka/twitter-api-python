
import enum
from enum import (
  auto,
)


class UserField(
  enum.Enum
):
  CREATED_AT = enum.auto()
  DESCRIPTION = enum.auto()
  ENTITIES = enum.auto()
  ID = enum.auto()
  LOCATION = enum.auto()
  NAME = enum.auto()
  PINNED_TWEET_ID = enum.auto()
  PROFILE_IMAGE_URL = (
    enum.auto()
  )
  PROTECTED = enum.auto()
  PUBLIC_METRICS = enum.auto()
  URL = enum.auto()
  USERNAME = enum.auto()
  VERIFIED = enum.auto()
  WITHHELD = enum.auto()

