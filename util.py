import pandas as pd
from pandas.core.frame import DataFrame
import numpy as np
import datetime as dt
from datetime import datetime
import plotly.graph_objects as go
from dash import Dash, dcc, html


def read_data(path: str, filename: str, column_index: str) -> DataFrame:
    fullpath = path + filename
    df = pd.read_csv(fullpath)
    df.set_index(column_index)
    return df


def check_date(d: str) -> bool:
    try:
        dt.date.fromisoformat(d)
    except ValueError:
        return False
    return True


def check_int(num: str) -> bool:
    try:
        int(num)
    except ValueError:
        return False
    return True


def check_null(v: str) -> bool:
    if v is not np.nan:
        return True
    return False


def check_day_of_week(d: str, business_date_number: int) -> bool:
    return datetime.strptime(d, '%Y-%m-%d').weekday() <= business_date_number


def unique_columns(df: DataFrame, columns: list) -> DataFrame:
    return df[df.duplicated(columns, keep=False)]


def save_csv_data(df: DataFrame, path: str, filename: str):
    fullpath = path + filename
    df.to_csv(fullpath)


def plot_candle_chart(df: DataFrame, yaxis_title: str, plot_axis: dict):
    fig = go.Figure(data=[go.Candlestick(x=df[plot_axis["x"]],
                                         open=df[plot_axis["open"]],
                                         high=df[plot_axis["high"]],
                                         low=df[plot_axis["low"]],
                                         close=df[plot_axis["close"]])])
    fig.update_layout(yaxis_title=yaxis_title)

    return fig


def agg_min(df: DataFrame, column: str) -> float:
    return df[column].min()


def agg_max(df: DataFrame, column: str) -> float:
    return df[column].max()


def agg_mean(df: DataFrame, column: str) -> float:
    return df[column].mean()
