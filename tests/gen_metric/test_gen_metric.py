from tests.test_case import TestCase
import transfrom as T
import util as U
import param as P
import validate as V
import gen_metric as G


class TestGenMetric(TestCase):
    def test_agg_min_max_avg_close_price(self):
        df = U.read_data(P.DATA_SOURCE_PATH, P.DATA_FILE_NAME, P.COLUMN_INDEX)
        df_dirty_removed = V.validate_dirty_data(df)
        df_clean_completed = V.validate_duplicate(df_dirty_removed, [P.COLUMN_INDEX])
        df_transform = T.transform_data(df_clean_completed)
        self.log(G.agg_min_max_avg_close_price(df_transform, P.DERIVATIVE_COLUMN))

    def test_calculate_avg_volume(self):
        df = U.read_data(P.DATA_SOURCE_PATH, P.DATA_FILE_NAME, P.COLUMN_INDEX)
        df_dirty_removed = V.validate_dirty_data(df)
        df_clean_completed = V.validate_duplicate(df_dirty_removed, [P.COLUMN_INDEX])
        df_transform = T.transform_data(df_clean_completed)
        self.log(G.calculate_avg_volume(df_transform, P.DERIVATIVE_VOLUME))

    def test_generate_metric(self):
        df = U.read_data(P.DATA_SOURCE_PATH, P.DATA_FILE_NAME, P.COLUMN_INDEX)
        df_dirty_removed = V.validate_dirty_data(df)
        df_clean_completed = V.validate_duplicate(df_dirty_removed, [P.COLUMN_INDEX])
        df_transform = T.transform_data(df_clean_completed)
        self.log(G.generate_metric(df_transform))
