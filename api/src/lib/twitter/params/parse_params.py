import typing
from typing import (
  Dict,
)
import dataclasses
from dataclasses import (
  fields,
)



class Params(
  typing.Protocol,
):

  __dataclass_field__: (
    typing.ClassVar[Dict[
      str,
      dataclasses.Field,
    ]]
  )




class ParseParams():
  def __call__(
    self,
    params: Params,
  ) -> typing.List[str]:
    ls = []
    for f in fields(params):
      f = f.name
      v = getattr(params, f)
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
    