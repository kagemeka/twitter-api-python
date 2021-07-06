import dataclasses


@dataclasses.dataclass
class Tweet():
  id: str
  text: str
  ...