import typing
from typing import (
  List,
)
import dataclasses
from dataclasses import (
  asdict,
)
import pandas as pd
from .fetch_keywords import (
  FetchKeywords,
)
from datetime import (
  datetime,
  timedelta,
)
from \
  lib.twitter.tweets \
  .search_tweets \
import (
  Params,
  MakeRequest,
)
from lib.twitter import (
  SendRequest,
)
from lib.twitter.tweets \
import (
  ConvertTweet,
  Tweet,
)
from lib.twitter.auth import (
  GetAuthFrom,
)


@dataclasses.dataclass
class Result():
  word: str
  tweet: Tweet
  


class GetTweets():
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
    convert = ConvertTweet()
    dt = datetime.now()
    end = dt - timedelta(
      seconds=10,
    )
    start = end - timedelta(
      days=1,
    )
    ls: List[Result] = []
    words = self.__keywords 
    for w in words:
      params = Params(query=w)
      params.start_time = start
      params.end_time = end
      f = params.tweet_fields
      f.created_at = True
      f.author_id = True
      f.public_metrics = True
      f.referenced_tweets = (
        True
      )
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
      tw = res.tweet
      w = res.word
      pm = tw.public_metrics
      data = {
        'search_word': w,
        'id': tw.id,
        'text': tw.text,
        'created_at': (
          tw.created_at
        ),
        'author_id': (
          tw.author_id
        ),
        **asdict(pm),
      }
      ls.append(data)
    self.__df = pd.DataFrame(
      ls,
    )