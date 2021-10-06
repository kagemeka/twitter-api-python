import typing
import dataclasses
from . import Params


class EnableAllParams():
  def __call__(
    self,
    params: Params,
  ) -> typing.NoReturn:
    for f in dataclasses.fields(params):
      f = f.name
      v = getattr(params, f)
      if type(v) != bool:
        self(v)
        continue
      setattr(params, f, True)
    