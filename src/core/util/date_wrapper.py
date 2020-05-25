import pandas as pd
import datetime
from datetime import datetime as datetime_2
from datetime import date, timedelta


class DateWrapper():
    def __init__(self):
        pass

    @staticmethod
    def get_date_range(start_date: str, end_date) -> list:
        dates = pd.date_range(start=start_date, end=end_date)

        dates_string = []
        for i in dates:
            dates_string.append(str(i.date()))

        return dates_string

    @staticmethod
    def get_date_range_datetime(start_date: str, end_date: str) -> list:
        dates = pd.date_range(start=start_date, end=end_date)

        dates_datetime = []
        for i in dates:
            dates_datetime.append(i.date())

        return dates_datetime

    @staticmethod
    def get_date_range_from_period(period: int = 28) -> list:
        dates = pd.date_range(end=datetime_2.today(), periods=period).to_pydatetime().tolist()

        dates_string = []
        for i in dates:
            dates_string.append(str(i.date()))

        return dates_string




