import typing


from .get_user_infos import (
  GetUserInfos,
)

from .get_tweets import (
  GetTweets,
)

from .get_tweet_counts import (
  GetTweetCounts,
)

from .make_df import (
  MakeAdamDF,
)

from .store import (
  Store,
)



class Adam():
  def __call__(
    self,
  ) -> typing.NoReturn:
    df = MakeAdamDF()()
    Store()(df)