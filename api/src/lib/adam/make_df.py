import dataclasses
import pandas as pd
import typing

from lib.adam import (
  GetUserInfos,
  GetTweets,
  GetTweetCounts,
)


@dataclasses.dataclass
class AdamDF():
  tweets: pd.DataFrame
  tweet_cnts: pd.DataFrame
  users: pd.DataFrame




class MakeAdamDF():
  def __call__(
    self,
  ) -> AdamDF:
    fns = (
      GetTweets(),
      GetTweetCounts(),
      GetUserInfos(),
    )
    return AdamDF(*(
      fn() for fn in fns
    ))
