import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class UserExpansions():
  pinned_tweet_id: bool = False

  NAME = 'expansions'