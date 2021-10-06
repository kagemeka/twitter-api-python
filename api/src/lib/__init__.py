import datetime 


class DatetimeToRFC3339():
  def __call__(
    self,
    dt: datetime.datetime,
  ) -> str:
    return f'{dt.isoformat()}Z'