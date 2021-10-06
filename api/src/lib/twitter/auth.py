import dataclasses
from typing import (
  Optional,
)
import typing 
import boto3 
import json



@dataclasses.dataclass
class TwitterAuth():
  api_key: Optional[str] = None
  api_secret_key: typing.Optional[str] = None
  bearer_token: Optional[str] = None
  access_token: Optional[str] = None
  access_secret_token: typing.Optional[str] = None



class GetTwitterAuth():  
  @classmethod
  def from_secrets_manager(
    cls, 
    secret_name: str,
  ) -> TwitterAuth:
    sm = boto3.client('secretsmanager')
    s = sm.get_secret_value(
      SecretId=secret_name,
    )['SecretString']
    s = json.loads(s)
    s = {
      k.lower(): v
      for k, v in s.items()
    }
    return TwitterAuth(**s)
  

  @classmethod
  def from_ssm_parameterstore(cls) -> TwitterAuth:
    ...