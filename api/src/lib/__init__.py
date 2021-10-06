import datetime 


class DatetimeFromStr():
  @staticmethod
  def rfc3339_format(s: str) -> datetime.datetime:
    f = '%Y-%m-%dT%H:%M:%S.%fZ'
    return datetime.strptime(s, f)


class DatetimeToRFC3339():
  def __call__(self, dt: datetime.datetime) -> str:
    return f'{dt.isoformat()}Z'