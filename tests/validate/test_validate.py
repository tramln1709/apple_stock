import stock_analyzer.param as P
import stock_analyzer.util as U
import stock_analyzer.validate as V
from tests.test_case import TestCase


class TestValidate(TestCase):
    def test_validate_dirty_data(self):
        df = U.read_data(P.DATA_SOURCE_PATH + P.DATA_FILE_NAME, P.COLUMN_INDEX)
        self.log(V.validate_dirty_data(df, P.DATA_OUT_PUT_PATH))

    def test_validate_duplicate(self):
        df = U.read_data(P.DATA_SOURCE_PATH + P.DATA_FILE_NAME, P.COLUMN_INDEX)
        self.log(V.validate_duplicate(df, P.COLUMN_INDEX, P.DATA_OUT_PUT_PATH))
