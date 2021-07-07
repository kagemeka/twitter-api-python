from pprint import (
  pprint,
)



from lib.adam import (
  GetUserInfos,
)


import typing
import boto3
import pandas as pd


class FetchComicKeywords():
  def __call__(
    self,
  ) -> typing.List[str]:
    self.__donwload_csv()
    self.__read_csv()
    self.__get_keywords()
    return self.__keywords
  

  def __get_keywords(
    self,
  ) -> typing.NoReturn:
    df = self.__df
    words = df.keyword.values
    self.__keywords = words
    

  def __read_csv(
    self,
  ) -> typing.NoReturn:
    self.__df = pd.read_csv(
      self.__save_path,
    )
  

  def __donwload_csv(
    self,
  ) -> typing.NoReturn:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(
      'av-adam-entrance',
    )
    ls = bucket.objects.filter(
      Prefix='natalie/',
    )
    ls = [o.key for o in ls]
    ls.sort()
    obj = ls[-1]
    self.__save_path = (
      '/tmp/data.csv'
    )
    bucket.Object(
      obj,
    ).download_file(
      self.__save_path,
    )




def main():
  # get = GetUserInfos()
  # users = get()
  
  # pprint(users)

  fetch = FetchComicKeywords()
  words = fetch()
  pprint(words)




  # s3 = boto3.resource('s3')
  # bucket = s3.Bucket(
  #   'av-adam-entrance',
  # )
  # print(
  #   *bucket.objects.all()
  # )
  


def lambda_handler(
  event,
  context,
):
  main()


if __name__ == '__main__':
  main()