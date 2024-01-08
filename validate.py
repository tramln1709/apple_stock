import mylogger
import param as P
import util as U
from pandas.core.frame import DataFrame
import pandas_schema
from pandas_schema.validation import CustomElementValidation
from pandas_schema import Column
import pandas as pd
logger = mylogger.get_logger()


def validate_dirty_data(df: DataFrame) -> DataFrame:
    try:
        logger.info('Clean Dirty Data Start')
        date_validation = [CustomElementValidation(lambda d: U.check_date(d), 'It should be YYYY-mm-dd')]
        int_validation = [CustomElementValidation(lambda d: U.check_price(d), 'is not positive integer')]
        null_validation = [CustomElementValidation(lambda d: U.check_null(d), 'this field cannot be null')]
        trend_validation = [CustomElementValidation(lambda d: U.check_trend(d), 'trend should be increasing or decreasing')]
        out_of_business_date = [
            CustomElementValidation(lambda d: U.check_day_of_week(d, P.BUSINESS_DATE_NUMBER), 'out of business date')]
        int_adjust = [CustomElementValidation(lambda d: U.check_adjust(d), 'is not integer')]

        schema = pandas_schema.Schema([
            Column("Date", date_validation + null_validation + out_of_business_date),
            Column("AAPL.Open", int_validation + null_validation),
            Column("AAPL.High", int_validation + null_validation),
            Column("AAPL.Low", int_validation + null_validation),
            Column("AAPL.Close", int_validation + null_validation),
            Column("AAPL.Volume", int_validation + null_validation),
            Column("AAPL.Adjusted", int_adjust + null_validation),
            Column("dn", int_validation + null_validation),
            Column("mavg", int_validation + null_validation),
            Column("up", int_validation + null_validation),
            Column("direction", trend_validation + null_validation)
        ])

        errors = schema.validate(df)
        errors_index_rows = [e.row for e in errors]
        data_clean = df.drop(index=errors_index_rows)
        U.save_csv_data(pd.DataFrame({'col': errors}), P.DATA_OUT_PUT_PATH, P.OUTPUT_ERROR_FILENAME)
        logger.info('Dirty File Saved at  {}{}'.format(P.DATA_OUT_PUT_PATH, P.OUTPUT_ERROR_FILENAME))
        logger.info('Clean Dirty Data End')
        return data_clean
    except Exception as e:
        logger.error(f"error in function validate_dirty_data {e}:e")


def validate_duplicate(df: DataFrame, columns: list) -> DataFrame:
    try:
        logger.info('Check Duplicate Data Start')
        df_duplicate = U.unique_columns(df, columns=columns)
        U.save_csv_data(df_duplicate, P.DATA_OUT_PUT_PATH, P.OUTPUT_ERROR_FILENAME_DUPLICATE)
        logger.info('Dirty File Saved at  {}{}'.format(P.DATA_OUT_PUT_PATH, P.OUTPUT_ERROR_FILENAME_DUPLICATE))
        df = df.drop_duplicates(subset=columns, keep=False)
        logger.info(
            'Data is cleaned and removed all of dirty data and duplicate data. Total records after clean is {0}'.format(
                len(df)))
        return df
    except Exception as e:
        logger.error(f"error in function validate_duplicate {e}:e")
