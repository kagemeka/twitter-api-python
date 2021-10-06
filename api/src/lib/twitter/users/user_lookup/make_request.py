from kgmk.twitter import Request
from . import (
  ByUsernameParams,
  ByIdParams,
  ByIdsParams,
  ByUsernamesParams,
)



class MakeRequest():
  @staticmethod
  def by_id(id_: str, params: ByIdParams) -> Request:
    api_path = f'/2/users/{id_}'
    return Request(api_path, params.to_dict())


  @staticmethod
  def by_ids(params: ByIdsParams) -> Request:
    api_path = '/2/users'
    return Request(api_path, params.to_dict())


  @staticmethod
  def by_username(
    username: str,
    params: ByUsernameParams,
  ) -> Request:
    api_path = f'/2/users/by/username/{username}' 
    return Request(api_path, params.to_dict())


  @staticmethod
  def by_usernames(params: ByUsernamesParams) -> Request:
    api_path = '/2/users/by'
    return Request(api_path, params.to_dict())
    