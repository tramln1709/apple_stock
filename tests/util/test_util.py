import pandas as pd

from stock_analyzer import param as P
from stock_analyzer import util as U
from tests.test_case import TestCase


class TestUtil(TestCase):

    def test_check_date_valid(self):
        self.log(U.check_date("2024-01-07"))

    def test_check_date_invalid_value(self):
        self.log(U.check_date("2024-13-07"))

    def check_price_valid(self):
        self.log(U.check_price("1.345"))

    def check_price_invalid(self):
        self.log(U.check_price("-1.345"))

    def test_check_adjust_valid(self):
        self.log(U.check_adjust("-189.45"))

    def test_check_adjust_invalid(self):
        self.log(U.check_adjust("aaaa"))

    def test_check_null_valid(self):
        self.log(U.check_null("d"))

    def test_check_null_invalid(self):
        self.log(U.check_null(""))

    def test_check_trend_valid(self):
        self.log(U.check_trend("Increasing"))

    def test_check_trend_invalid(self):
        self.log(U.check_trend("Down"))

    def test_check_date_of_week_valid(self):
        self.log(U.check_day_of_week("2013-03-12", 4))

    def test_check_date_of_week_invalid(self):
        self.log(U.check_day_of_week("2024-01-07", 4))

    def test_agg_min(self):
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        df = pd.DataFrame(data, columns=['Name', 'Age'])
        self.log(U.agg_min(df, "Age"))

    def test_agg_max(self):
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        df = pd.DataFrame(data, columns=['Name', 'Age'])
        self.log(U.agg_max(df, "Age"))

    def test_agg_mean(self):
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        df = pd.DataFrame(data, columns=['Name', 'Age'])
        self.log(U.agg_mean(df, "Age"))

    def test_unique_columns_invalid(self):
        data = [['tom', 10], ['nick', 15], ['juli', 14], ['tom', 10]]
        df = pd.DataFrame(data, columns=['Name', 'Age'])
        self.log(U.unique_columns(df, ["Name"]))

    def test_unique_columns_valid(self):
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        df = pd.DataFrame(data, columns=['Name', 'Age'])
        self.log(U.unique_columns(df, ["Name"]))

    def test_read_data(self):
        self.log(U.read_data(P.DATA_SOURCE_PATH + P.DATA_FILE_NAME, "Date"))
