import dataclasses
import requests
import typing
from .auth import TwitterAuth



@dataclasses.dataclass
class Request():
  api_path: str
  params: dict



def send_request(
  auth: TwitterAuth,
  request: Request,
) -> requests.models.Response:
  BASE_URL = 'https://api.twitter.com' 
  token = f'Bearer {auth.bearer_token}'
  return requests.get(
    url=f'{BASE_URL}{request.api_path}',
    headers={'Authorization': token},
    params=request.params,
  )


class SendRequest():
  def __call__(
    self, 
    request: Request,
  ) -> requests.models.Response:
    url = self.__base_url
    path = request.api_path
    url = f'{url}{path}'
    response = requests.get(
      url=url,
      headers=self.__headers,
      params=request.params,
    )
    return response
  

  def __init__(
    self,
    auth: TwitterAuth,
  ) -> typing.NoReturn:
    token = f'Bearer {auth.bearer_token}'
    self.__headers = {'Authorization': token}
    self.__base_url = 'https://api.twitter.com'