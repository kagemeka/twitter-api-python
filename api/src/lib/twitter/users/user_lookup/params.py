import dataclasses
import typing
from .. import Expansions
from ...fields import TweetFields, UserFields
from ... import ConvertParams



@dataclasses.dataclass
class Params():
  expansions: Expansions = Expansions()
  tweet_fields: TweetFields = TweetFields()
  user_fields: UserFields = UserFields()


  def to_dict(self) -> dict:
    convert = ConvertParams()
    params = (
      self.expansions,
      self.tweet_fields,
      self.user_fields,
    )
    return {
      p.name: p.string
      for p in map(convert, params)
    }



@dataclasses.dataclass
class ByIdParams(Params): ...



@dataclasses.dataclass
class ByIdsParams(Params):
  ids: typing.List[str] = dataclasses.field(
    default_factory=list,
  )


  def to_dict(self) -> dict:
    return {
      'ids': ','.join(self.ids),
      **super().to_dict(),
    }



@dataclasses.dataclass
class ByUsernameParams(Params): ...



@dataclasses.dataclass
class ByUsernamesParams(Params):
  usernames: typing.List[str] = dataclasses.field(
    default_factory=list,
  )


  def to_dict(self) -> dict:
    print(','.join(self.usernames))
    return {
      'usernames': ','.join(self.usernames),
      **super().to_dict(),
    }