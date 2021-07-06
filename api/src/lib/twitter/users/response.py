import dataclasses
import typing
from typing import (
  Optional,
)
import requests
from .user import (
  User,
  ParseUser,
)
from .includes import (
  Includes,
  ParseIncludes,
)



@dataclasses.dataclass
class Response:
  data: User
  includes: Optional[
    Includes
  ] = None
  errors: Optional[
    dict # TODO change later
  ] = None



class ParseResponse():
  
  def __call__(
    self,
    response: (
      requests.models.Response
    ), 
  ) -> Response:
    self.__res = response
    self.__parse()
    return self.__res
  

  def __parse(
    self,
  ) -> typing.NoReturn:
    self.__res = Response(
      **self.__res.json(),
    )
    self.__data()
    self.__includes()
    self.__errors()
  
  
  def __data(
    self,
  ) -> typing.NoReturn:
    res = self.__res
    if res.data is None:
      return
    res.data = ParseUser()(
      res.data,
    )
  
  def __includes(
    self,
  ) -> typing.NoReturn:
    res = self.__res
    if res.includes is None:
      return
    parse = ParseIncludes()
    res.includes = parse(
      res.includes,
    )
  

  def __errors(
    self,
  ) -> typing.NoReturn:
    ... 
    