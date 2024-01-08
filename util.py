import subprocess

import pandas as pd
from pandas.core.frame import DataFrame
import datetime as dt
from datetime import datetime
import plotly.graph_objects as go


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


def check_price(num: str) -> bool:
    try:
        if float(num) > 0:
            return True
    except ValueError:
        return False


def check_adjust(num: str) -> bool:
    try:
        float(num)
    except ValueError:
        return False
    return True


def check_null(v: str) -> bool:
    if v:
        return True
    return False


def check_trend(v: str) -> bool:
    if v not in ["Increasing", "Decreasing"]:
        return False
    return True


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


def exec_shell_cmd(command):
    if not command:
        raise Exception("Invalid command: {}".format(command))

    proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    std_out, std_err = proc.communicate()
    message = std_out.decode("utf-8")
    code = proc.returncode
    if message and code != 0:
        raise Exception("exec shell command with error: {}".format(message))
    else:
        return message
