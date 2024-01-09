import pandas as pd
from pandas import DataFrame

import param as P
import util as U
import mylogger as L

logger = L.get_logger()


def agg_min_max_avg_close_price(df: DataFrame, derivative_column: str) -> DataFrame:
    try:
        logger.info('Calculate avg/min/max of {}'.format(derivative_column))
        max_value = U.agg_max(df, derivative_column)
        min_value = U.agg_min(df, derivative_column)
        avg_value = U.agg_mean(df, derivative_column)
        logger.info(
            'Calculate avg Volume End with max = {0} , min = {1} , avg = {2} '.format(max_value, min_value, avg_value))
        return pd.DataFrame([{"max_price": [max_value], "min_price": [min_value], "avg_price": [avg_value]}])
    except Exception as e:
        logger.error(f"error in function agg_min_max_avg_close_price {e}:e")


def calculate_avg_volume(df: DataFrame, derivative_column: str) -> float:
    try:
        logger.info('Calculate avg Volume Start ')
        avg_volume_value = U.agg_mean(df, derivative_column)
        return avg_volume_value
    except Exception as e:
        logger.error("error in function calculate_avg_volume {}:".format(e))


def save_exceed_avg_volume(df: DataFrame, derivative_column: str, avg_volume: float, output_dir) -> DataFrame:
    try:
        logger.info("Save exceed avg volume Start")
        df = df.query("`{}` > @avg_volume ".format(derivative_column))
        logger.info('Exceeded file saved at {}{}'.format(output_dir, P.OUTPUT_EXCEEDED_FILENAME))
        U.save_csv_data(pd.DataFrame(df), output_dir, P.OUTPUT_EXCEEDED_FILENAME)
        logger.info("Save exceed avg volume End")
        return df
    except Exception as e:
        logger.error(f"error in function save_exceed_avg_volume {e}:e")


def generate_metric(df: DataFrame) -> DataFrame:
    try:
        logger.info('Generate Metric Start ')
        df_agg = df.groupby(["week_of_year"])[["AAPL.Close", "AAPL.Low", "AAPL.High", "AAPL.Open"]].mean().reset_index()
        logger.info('Generate Metric End ')
        return df_agg.sort_values("week_of_year", ascending=[True])
    except Exception as e:
        logger.error(f"error in function generate_metric {e}:e")
