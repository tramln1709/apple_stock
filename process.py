import mylogger
import util as U
import param as P
import validate as V
import transfrom as T
import gen_metric as G
from pandas.core.frame import DataFrame

from dash import Dash, dcc, html

logger = mylogger.get_logger()


def process_data() -> list[DataFrame]:
    logger.info(
        'Read data source from path {0}{1} and start processing data'.format(P.DATA_SOURCE_PATH, P.DATA_FILE_NAME))
    df_source = U.read_data(P.DATA_SOURCE_PATH, P.DATA_FILE_NAME, P.COLUMN_INDEX)
    logger.info("Data source with {0} records".format(len(df_source)))
    df_dirty_data_removed = V.validate_dirty_data(df_source)
    df_data_clean = V.validate_duplicate(df_dirty_data_removed, [P.COLUMN_INDEX])
    df_data_transformed = T.transform_data(df_data_clean)
    G.agg_min_max_avg_close_price(df_data_transformed, P.DERIVATIVE_COLUMN)
    G.calculate_avg_volume(df_data_transformed, P.DERIVATIVE_VOLUME)
    df_data_analyze = G.generate_metric(df_data_transformed)
    logger.info('Process end')

    return [df_data_analyze, df_data_transformed]


if __name__ == "__main__":
    list_data = process_data()

    app = Dash()

    app.layout = html.Div([
        html.Div([html.H1("The mean weekly stock price of Apple throughout the year")],
                 style={'width': "90%", "margin": "auto", "text-align": "center"}),
        html.Div(
            dcc.Graph(id="weekly_graph",
                      figure=U.plot_candle_chart(list_data[0], "Apple Stock", P.PLOT_AXIS_WEEK_MEAN))),
        html.Div([html.H1("The mean daily stock price of Apple throughout the year")],
                 style={'width': "90%", "margin": "auto", "text-align": "center"}),
        html.Div(
            dcc.Graph(id="daily_graph",
                      figure=U.plot_candle_chart(list_data[1], "Apple Stock", P.PLOT_AXIS_WEEK_DAY))),
    ])

    app.run_server(host="0.0.0.0", port=8080, debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
