import mylogger
from pandas.core.frame import DataFrame
import pandas as pd
logger = mylogger.get_logger()

def transform_data(df: DataFrame) -> DataFrame:
    try:
        logger.info('Transform Data Start')
        df['day_of_week'] = pd.to_datetime(df['Date']).dt.day_name()
        df['Week_of_Year'] = pd.to_datetime(df['Date']).dt.strftime('%Y%U')
        logger.info('Transform Data End')
        return df
    except Exception as e:
        logger.error(f"error in function transform_data {e}:e")