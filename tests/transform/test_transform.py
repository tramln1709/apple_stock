from tests.test_case import TestCase
import transfrom as T
import util as U
import param as P
import validate as V


class TestTransform(TestCase):
    def check_transform_data(self):
        df = U.read_data(P.DATA_SOURCE_PATH, P.DATA_FILE_NAME, P.COLUMN_INDEX)
        df_dirty_removed = V.validate_dirty_data(df)
        df_clean_completed = V.validate_duplicate(df_dirty_removed, P.COLUMN_INDEX)
        self.log(T.transform_data(df_clean_completed))
