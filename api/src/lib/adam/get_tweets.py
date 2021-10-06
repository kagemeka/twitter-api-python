import typing
import dataclasses
import pandas as pd
import tqdm
import datetime 
from ._fetch_keywords import _fetch_keywords
from lib.twitter.tweets.search_tweets import (
  Params,
  MakeRequest,
)
from lib.twitter import SendRequest
from lib.twitter.tweets import Tweet, ConvertTweet
from lib.twitter.auth import GetTwitterAuth
from lib.aws_util.s3.download import download_from_s3
from lib.aws_util.s3.upload import upload_to_s3



@dataclasses.dataclass
class Result():
  word: str
  tweet: Tweet
  


def get_tweets() -> typing.NoReturn:
  SECRET_NAME = 'adam-twitter'
  auth = GetTwitterAuth.from_secrets_manager(SECRET_NAME)
  send = SendRequest(auth)
  dt = datetime.datetime.now()
  end = dt - datetime.timedelta(seconds=10)
  start = end - datetime.timedelta(days=1)
  results: typing.List[Result] = []
  for word in tqdm.tqdm(_fetch_keywords()):
    params = Params(query=word)
    params.start_time = start
    params.end_time = end
    f = params.tweet_fields
    f.created_at = True
    f.author_id = True
    f.public_metrics = True
    f.referenced_tweets = True
    req = MakeRequest()(params)
    res = send(req).json()
    data = res.get('data', None)
    if data is None: continue
    for tw in data:
      results.append(Result(word, ConvertTweet()(tw)))
  ls = [
    {
      'search_word': res.word,
      'id': res.tweet.id,
      'text': res.tweet.text,
      'created_at': res.tweet.created_at,
      'author_id': res.tweet.author_id,
      **dataclasses.asdict(res.tweet.public_metrics),
    }
    for res in results 
  ]
  df = pd.DataFrame(ls)
  __store(df)


def __store(df: pd.DataFrame) -> typing.NoReturn:
  bucket = 'av-adam-store'
  save_path = '/tmp/tweets.csv'
  obj = 'twitter/tweets.csv'
  date = str(datetime.datetime.now().date())
  df['updated_at'] = date
  download_from_s3(bucket, obj, save_path)
  old_df = pd.read_csv(save_path)
  df = pd.concat((old_df, df), ignore_index=True)
  df['id'] = df.id.astype(str)
  df.drop_duplicates(subset=['id'], inplace=True)
  print(df)
  df.to_csv(save_path, index=False)
  upload_to_s3(bucket, obj, save_path)
