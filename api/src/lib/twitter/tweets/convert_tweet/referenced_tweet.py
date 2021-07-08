import typing
import dataclasses
from typing import (
  Optional,
)



@dataclasses.dataclass
class ReferencedTweet():
  type: str
  id: str
  




class ConvertReferencedTweet():
  def __call__(
    self,
    data: dict,
  ) -> ReferencedTweet:
    self.__data = data
    self.__convert()
    return self.__tw
  
  
  def __convert(
    self,
  ) -> typing.NoReturn:
    tw = ReferencedTweet(
      **self.__data,
    )
    self.__tw = tw
     