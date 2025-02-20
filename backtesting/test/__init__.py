"""Data and utilities for testing."""
import pandas as pd


def _read_file(filename):
    from os.path import dirname, join

    return pd.read_csv(join(dirname(__file__), filename),
                       index_col=0, parse_dates=True)



GOOG = _read_file('GOOG.csv')
"""DataFrame of daily NASDAQ:GOOG (Google/Alphabet) stock price data from 2004 to 2013."""

EURUSD = _read_file('EURUSD.csv')
"""DataFrame of hourly EUR/USD forex data from April 2017 to February 2018."""


def csvconverter(fname):
    print(fname)
    f=pd.read_csv(fname)
    keep_col = ['j','t','Open','High','Low','Close','Volume']
    new_f = f[keep_col]
    new_f['j'] = pd.to_datetime(new_f['j'], format='%Y%m%d')
    new_f['t'] = pd.to_datetime(new_f['t'], format='%H%M%S')
    new_f['t'] = new_f['t'].dt.strftime('%H:%M:%S')
    new_f.to_csv(f"new_{fname}.csv", index=False)
        
def SMA(arr: pd.Series, n: int) -> pd.Series:
    """
    Returns `n`-period simple moving average of array `arr`.
    """
    return pd.Series(arr).rolling(n).mean()
