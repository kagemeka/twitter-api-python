import dataclasses



@dataclasses.dataclass
class Expansions():
  pinned_tweet_id: bool = False

  NAME = 'expansions'