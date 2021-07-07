import typing
from typing import (
  Dict,
)
import dataclasses
from dataclasses import (
  fields,
)



class Param(
  typing.Protocol,
):

  __dataclass_field__: (
    typing.ClassVar[Dict[
      str,
      dataclasses.Field,
    ]]
  )




class ParseParam():
  def __call__(
    self,
    param: Param,
  ) -> typing.List[str]:
    self.__param = param
    return self.__parse()


  def __parse(
    self,
  ) -> typing.List[str]:
    param = self.__param
    ls = []
    for f in fields(param):
      f = f.name
      v = getattr(param, f)
      if v is None: continue
      if v == False: continue
      if v == True:
        ls.append(f); continue
      ls += [
        f if s == 'self_'
        else f'{f}.{s}'  
        for s in self(v)
      ]
    return ls
    