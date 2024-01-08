from tests.test_case import TestCase
import validate as V
import util as U
import param as P


class TestValidate(TestCase):
    def test_validate_dirty_data(self):
        df = U.read_data(P.DATA_SOURCE_PATH, P.DATA_FILE_NAME, P.COLUMN_INDEX)
        self.log(V.validate_dirty_data(df))

    def test_validate_duplicate(self):
        df = U.read_data(P.DATA_SOURCE_PATH, P.DATA_FILE_NAME, P.COLUMN_INDEX)
        self.log(V.validate_duplicate(df,P.COLUMN_INDEX))
