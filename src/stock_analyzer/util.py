import datetime as dt
import os.path
import subprocess
from datetime import datetime

import pandas as pd
import plotly.graph_objects as go
from pandas.core.frame import DataFrame


def read_data(filename: str, column_index: str) -> DataFrame:
    df = pd.read_csv(filename)
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
    try:
        return datetime.strptime(d, '%Y-%m-%d').weekday() <= business_date_number
    except:
        return False


def unique_columns(df: DataFrame, columns: list) -> DataFrame:
    return df[df.duplicated(columns, keep=False)]


def save_csv_data(df: DataFrame, path: str, filename: str):
    fullpath = os.path.join(path, filename)
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


def check_file_existing(file_path):
    """
    check if file is existing
    :param file_path:
    :return: True if existing otherwise return False
    """
    return os.path.isfile(file_path)


def check_writing_permission(directory_path):
    """
    check if the user has writing permission on the input dir
    :param directory_path:
    :return: True if the use has writing permission otherwise False
    """
    permissions = os.stat(directory_path).st_mode
    return permissions & 0o200
