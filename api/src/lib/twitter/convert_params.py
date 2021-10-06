import typing
import dataclasses


@dataclasses.dataclass
class Param():
  name: str
  string: str



class Params(typing.Protocol):
  __dataclass_field__: typing.ClassVar[
    typing.Dict[str, dataclasses.Field]
  ]

  NAME: typing.Optional[str]
  


class ConvertParams():
  def __call__(self, params: Params) -> Param:
    ls = self.__dfs(params)
    s = ','.join(ls)
    name = params.NAME
    return Param(name, s)

  
  @classmethod
  def __dfs(cls, params: Params) -> typing.List[str]:
    ls = []
    for f in dataclasses.fields(params):
      f = f.name
      v = getattr(params, f)
      if v == False: continue
      if v == True:
        ls.append(f); continue
      ls += [
        f if s == 'self_'
        else f'{f}.{s}'  
        for s in cls.__dfs(v)
      ]
    return ls
    