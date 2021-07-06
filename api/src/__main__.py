from __future__ import (
  annotations,
)
import typing
import dataclasses
from typing import (
  Optional,
)
from datetime import (
  datetime,
)
import boto3

import pandas as pd

from pprint import (
  pprint,
)



import enum
from enum import (
  auto,
)



from dataclasses import (
  asdict,
  fields,
)


from lib.adam import (
  GetUserInfos,
)



def main():
  get = GetUserInfos()
  users = get()
  
  pprint(users)

  # s3 = boto3.resource('s3')
  # bucket = s3.Bucket(
  #   'av-adam-entrance',
  # )
  # print(
  #   *bucket.objects.all()
  # )
  



if __name__ == '__main__':
  main()