from stock_analyzer import param as P
from stock_analyzer import transform as T
from stock_analyzer import util as U
from stock_analyzer import validate as V
from tests.test_case import TestCase


class TestTransform(TestCase):
    def test_transform_data(self):
        df = U.read_data(P.DATA_SOURCE_PATH + P.DATA_FILE_NAME, P.COLUMN_INDEX)
        df_dirty_removed = V.validate_dirty_data(df, P.DATA_OUT_PUT_PATH)
        df_clean_completed = V.validate_duplicate(df_dirty_removed, P.COLUMN_INDEX, P.DATA_OUT_PUT_PATH)
        self.log(T.transform_data(df_clean_completed))
