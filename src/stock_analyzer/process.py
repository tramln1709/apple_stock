import os

from dash import Dash, dcc, html
from pandas import DataFrame

import gen_metric as G
import my_errors as E
import mylogger as L
import param as P
import transform as T
import util as U
import validate as V

logger = L.get_logger()


def clean_transform(data_file: str, output_dir: str) -> DataFrame:
    """
    clean data: remove wrongly format and duplicated data
    transform data: add new two columns which are 'dau_of_week' and 'week_of_year'

    :param data_file: csv data file
    :return: data transformed. raise error if inputs invalid
    """
    if not U.check_file_existing(data_file):
        raise E.InputError("datafile", data_file)

    if not U.check_writing_permission(output_dir):
        raise E.InputError("output_dir", output_dir)

    logger.info('Read data source from path {0} and start processing data'.format(data_file))
    df_source = U.read_data(data_file, P.COLUMN_INDEX)
    logger.info("Data source with {0} records".format(len(df_source)))
    df_dirty_data_removed = V.validate_dirty_data(df_source, output_dir)
    df_data_clean = V.validate_duplicate(df_dirty_data_removed, [P.COLUMN_INDEX], output_dir)
    df_transformed = T.transform_data(df_data_clean)
    return df_transformed


def agg_data(df: DataFrame, output_dir) -> DataFrame:
    """

    :param df:
    :return:
    """
    G.agg_min_max_avg_close_price(df, P.DERIVATIVE_COLUMN)
    avg_volume = G.calculate_avg_volume(df, P.DERIVATIVE_VOLUME)
    G.save_exceed_avg_volume(df, P.DERIVATIVE_VOLUME, avg_volume, output_dir)
    df = G.generate_metric(df)
    logger.info('Process end')

    return df


def stock_analyze(input_file, output_dir):
    try:
        df_transformed = clean_transform(input_file, output_dir)
        df_analyze = agg_data(df_transformed, output_dir)
    except Exception as e:
        print(e)
    else:
        app = Dash()
        app.layout = html.Div([
            html.Div([html.H1("The mean weekly stock price of Apple throughout the year")],
                     style={'width': "90%", "margin": "auto", "text-align": "center"}),
            html.Div(
                dcc.Graph(id="weekly_graph",
                          figure=U.plot_candle_chart(df_analyze, "Apple Stock", P.PLOT_AXIS_WEEK_MEAN))),
            html.Div([html.H1("The mean daily stock price of Apple throughout the year")],
                     style={'width': "90%", "margin": "auto", "text-align": "center"}),
            html.Div(
                dcc.Graph(id="daily_graph",
                          figure=U.plot_candle_chart(df_transformed, "Apple Stock", P.PLOT_AXIS_WEEK_DAY))),
        ])

        app.run_server(host="0.0.0.0", port=8080, debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter


if __name__ == "__main__":
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIR = os.path.join(FILE_DIR, "..")
    input_file = os.path.join(PROJECT_DIR, "data_source", "finance-charts-apple.csv")
    output_dir = os.path.join(PROJECT_DIR, "data_output")
    stock_analyze(input_file, output_dir)
