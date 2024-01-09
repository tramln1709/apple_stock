import os

from stock_analyzer import gen_metric as G
from stock_analyzer import param as P
from stock_analyzer import transform as T
from stock_analyzer import util as U
from stock_analyzer import validate as V
from tests.test_case import TestCase


class TestGenMetric(TestCase):
    def test_agg_min_max_avg_close_price(self):
        df = U.read_data(P.DATA_SOURCE_PATH + P.DATA_FILE_NAME, P.COLUMN_INDEX)
        df_dirty_removed = V.validate_dirty_data(df, P.DATA_OUT_PUT_PATH)
        df_clean_completed = V.validate_duplicate(df_dirty_removed, [P.COLUMN_INDEX], P.DATA_OUT_PUT_PATH)
        df_transform = T.transform_data(df_clean_completed)
        self.log(G.agg_min_max_avg_close_price(df_transform, P.DERIVATIVE_COLUMN))

    def test_calculate_avg_volume(self):
        df = U.read_data(os.path.join(P.DATA_SOURCE_PATH, P.DATA_FILE_NAME), P.COLUMN_INDEX)
        df_dirty_removed = V.validate_dirty_data(df, P.DATA_OUT_PUT_PATH)
        df_clean_completed = V.validate_duplicate(df_dirty_removed, [P.COLUMN_INDEX], P.DATA_OUT_PUT_PATH)
        df_transform = T.transform_data(df_clean_completed)
        self.log(G.calculate_avg_volume(df_transform, P.DERIVATIVE_VOLUME))

    def test_save_exceed_avg_volume(self):
        df = U.read_data(os.path.join(P.DATA_SOURCE_PATH, P.DATA_FILE_NAME), P.COLUMN_INDEX)
        df_dirty_removed = V.validate_dirty_data(df, P.DATA_OUT_PUT_PATH)
        df_clean_completed = V.validate_duplicate(df_dirty_removed, [P.COLUMN_INDEX], P.DATA_OUT_PUT_PATH)
        df_transform = T.transform_data(df_clean_completed)
        avg_volume = G.calculate_avg_volume(df_transform, P.DERIVATIVE_VOLUME)
        self.log(G.save_exceed_avg_volume(df_transform, P.DERIVATIVE_VOLUME, avg_volume, P.DATA_OUT_PUT_PATH))

    def test_generate_metric(self):
        df = U.read_data(P.DATA_SOURCE_PATH + P.DATA_FILE_NAME, P.COLUMN_INDEX)
        df_dirty_removed = V.validate_dirty_data(df, P.DATA_OUT_PUT_PATH)
        df_clean_completed = V.validate_duplicate(df_dirty_removed, [P.COLUMN_INDEX], P.DATA_OUT_PUT_PATH)
        df_transform = T.transform_data(df_clean_completed)
        self.log(G.generate_metric(df_transform))
