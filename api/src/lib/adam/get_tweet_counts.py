import typing
import dataclasses
import pandas as pd
import datetime 
import tqdm 
from ._fetch_keywords import _fetch_keywords
from lib.twitter.auth import TwitterAuth, GetTwitterAuth
from lib.twitter.tweets.tweet_counts import (
  MakeRequest,
  Params,
  ConvertTweetCount,
  TweetCount,
)
from lib.twitter import SendRequest
from lib.aws_util.s3.download import download_from_s3
from lib.aws_util.s3.upload import upload_to_s3



@dataclasses.dataclass
class Result():
  word: str
  tweet_count : TweetCount
  


def get_tweet_counts() -> typing.NoReturn:
  SECRET_NAME = 'adam-twitter'
  auth = GetTwitterAuth.from_secrets_manager(SECRET_NAME)
  send = SendRequest(auth)
  dt = datetime.datetime.now()
  end = dt - datetime.timedelta(seconds=10)
  start = end - datetime.timedelta(days=1)
  results: typing.List[Result] = []
  for word in tqdm.tqdm(_fetch_keywords()):
    params = Params(query=word)
    params.start_time, params.end_time = start, end 
    res = send(MakeRequest()(params)).json()
    data = res.get('data', None)
    if data is None: continue
    for tw in data:
      results.append(Result(word, ConvertTweetCount()(tw)))
  ls = [
    {
      'search_word': res.word,
      **dataclasses.asdict(res.tweet_count),
    }
    for res in results 
  ]
  df = pd.DataFrame(ls)
  __store(df)



def __store(df: pd.DataFrame) -> typing.NoReturn:
  bucket = 'av-adam-store'
  save_path = '/tmp/tweet_counts.csv'
  obj = 'twitter/tweet_counts.csv'
  date = str(datetime.datetime.now().date())
  df['updated_at'] = date
  download_from_s3(bucket, obj, save_path)
  old_df = pd.read_csv(save_path)
  df = pd.concat((old_df, df), ignore_index=True)
  df[['start', 'end']] = df[['start', 'end']].astype(str)
  df.drop_duplicates(
    subset=['search_word', 'start', 'end'], 
    inplace=True,
  )
  print(df)
  df.to_csv(save_path, index=False)
  upload_to_s3(bucket, obj, save_path)
