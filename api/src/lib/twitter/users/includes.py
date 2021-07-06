import dataclasses
import typing
from lib.twitter.tweets import(
  Tweet,
)



@dataclasses.dataclass
class Includes():
  tweets: typing.List[Tweet]



class ParseIncludes():
  def __call__(
    self,
    data: dict,
  ) -> Includes:
    self.__data = data
    self.__parse()
    return self.__includes
  

  def __parse(
    self,
  ) -> typing.NoReturn:
    includes = Includes(
      **self.__data,
    )
    self.__includes = includes
    self.__tweets()


  def __tweets(
    self,
  ) -> typing.NoReturn:
    includes = self.__includes
    if includes.tweets is None:
      return
    includes.tweets = [
      Tweet(**tw)
      for tw in includes.tweets
    ] 
     