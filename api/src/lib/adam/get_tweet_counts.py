import typing
from typing import (
  List,
)
import dataclasses
from dataclasses import (
  asdict,
)
import pandas as pd
from datetime import (
  datetime,
  timedelta,
)
from tqdm import (
  tqdm,
)
from .fetch_keywords import (
  FetchKeywords,
)
from kgmk.twitter.auth import (
  GetAuthFrom,
)

from \
  kgmk.twitter.tweets \
  .tweet_counts \
import (
  MakeRequest,
  Params,
  ConvertTweetCount,
  TweetCount,
)

from kgmk.twitter import (
  SendRequest,
)


@dataclasses.dataclass
class Result():
  word: str
  tweet_count : TweetCount
  


class GetTweetCounts():
  def __call__(
    self,
  ) -> pd.DataFrame:
    self.__get_keywords()
    self.__set_auth()
    self.__request()
    self.__to_dataframe()
    return self.__df
  

  def __set_auth(
    self,
  ) -> typing.NoReturn:
    get = GetAuthFrom()
    auth = get.secrets_manager(
      'adam-twitter',
    )
    self.__auth = auth
  
  
  def __get_keywords(
    self,
  ) -> typing.NoReturn:
    self.__keywords = (
      FetchKeywords()()
    )

  
  def __request(
    self,
  ) -> typing.NoReturn:
    auth = self.__auth
    send = SendRequest(auth)
    make = MakeRequest()
    convert = (
      ConvertTweetCount()
    )
    dt = datetime.now()
    end = dt - timedelta(
      seconds=10,
    )
    start = end - timedelta(
      days=1,
    )
    ls: List[Result] = []
    words = self.__keywords 
    for w in tqdm(words):
      params = Params(query=w)
      params.start_time = start
      params.end_time = end
      req = make(params)
      res = send(req).json()
      data = res.get(
        'data',
        None,
      )
      if data is None: continue
      for tw in data:
        ls.append(Result(
          w, convert(tw),
        ))
    self.__tweets = ls

  
  def __to_dataframe(
    self,
  ) -> typing.NoReturn:
    tweets = self.__tweets
    ls = []
    for res in tweets: 
      w = res.word
      data = {
        'search_word': w,
        **asdict(
          res.tweet_count,
        ),
      }
      ls.append(data)
    self.__df = pd.DataFrame(
      ls,
    )