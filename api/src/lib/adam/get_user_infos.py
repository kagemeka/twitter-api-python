import typing
import dataclasses
import pandas as pd
from lib.twitter.users.user_lookup import (
  ByUsernamesParams,
  MakeRequest,
)
import datetime 
from lib.twitter import SendRequest
from lib.twitter.users import ConvertUser
from lib.twitter.auth import GetTwitterAuth
from lib.aws_util.s3.download import download_from_s3
from lib.aws_util.s3.upload import upload_to_s3



def _fetch_usernames() -> typing.NoReturn:
  bucket = 'av-adam-store'
  save_path = '/tmp/meta.csv'
  obj = 'akibasouken/meta.csv'
  download_from_s3(bucket, obj, save_path)
  df = pd.read_csv(save_path)
  return df.twitter_username.dropna().values



def get_user_infos() -> typing.NoReturn:
  SECRET_NAME = 'adam-twitter'
  auth = GetTwitterAuth.from_secrets_manager(SECRET_NAME)
  params = ByUsernamesParams(usernames=_fetch_usernames())
  params.user_fields.public_metrics = True
  send = SendRequest(auth)
  res = send(MakeRequest.by_usernames(params)).json()
  convert = ConvertUser()
  print(res)
  users = [convert(user) for user in res['data']]
  ls = []
  for user in users:
    data = {
      'id': user.id,
      'name': user.name,
      'username': user.username,
      **dataclasses.asdict(user.public_metrics),
    }
    ls.append(data)
  df = pd.DataFrame(ls)
  __store(df)


def __store(df: pd.DataFrame) -> typing.NoReturn:
  bucket = 'av-adam-store'
  save_path = '/tmp/users.csv'
  obj = 'twitter/users.csv'
  date = str(datetime.datetime.now().date())
  df['updated_at'] = date
  download_from_s3(bucket, obj, save_path)
  old_df = pd.read_csv(save_path)
  df = pd.concat((old_df, df), ignore_index=True)
  df['id'] = df.id.astype(str)
  df.drop_duplicates(
    subset=['id', 'updated_at'],
    keep='last',
    inplace=True,
  )
  print(df)
  df.to_csv(save_path, index=False)
  upload_to_s3(bucket, obj, save_path)

