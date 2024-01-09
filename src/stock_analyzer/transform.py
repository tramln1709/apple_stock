from stock_analyzer.mylogger import get_logger
import pandas as pd
from pandas.core.frame import DataFrame

logger = get_logger()


def transform_data(df: DataFrame) -> DataFrame:
    try:
        logger.info('Transform Data Start')
        df['day_of_week'] = pd.to_datetime(df['Date']).dt.day_name()
        df['week_of_year'] = pd.to_datetime(df['Date']).dt.strftime('%Y%U')
        logger.info('Transform Data End')
        print(df.head(5))
        return df
    except Exception as e:
        logger.error(f"error in function transform_data {e}:e")
