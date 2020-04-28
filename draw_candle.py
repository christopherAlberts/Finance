import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader as web
from mplfinance.original_flavor import candlestick_ohlc

def draw_candle(tick, period):

    file = tick + '.csv'

    style.use('ggplot')

    start = dt.datetime(2000,1,1)
    end = dt.datetime.now()

    df = web.DataReader(tick , 'yahoo', start, end)
    df.to_csv(file) # Create .csv

    # print(df.head(5))

    style.use('ggplot')

    df = pd.read_csv(file, parse_dates=True, index_col=0)
    # df['100ma'] = df['Adj Close'].rolling(window=100).mean()  # Create a new column for 100 moving average

    # ohlc = Open High Low Close
    df_ohlc = df['Adj Close'].resample(period).ohlc()  # period='10D' Resample 10 days, can also do week year ...
    df_volume = df['Volume'].resample(period).sum()

    df_ohlc.reset_index(inplace=True)
    df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)  # mdates maked date to some weird 7090834 number that matplotlib will use

    # print(df_ohlc.head())

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)  # (Grid size, Starting point, rowspan, colspan)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)  # (Grid size, Starting point, rowspan, colspan, share x)
    ax1.xaxis_date()
    ax1.set_facecolor("#eafff5")


    candlestick_ohlc(ax1, df_ohlc.values, width=4, colorup= 'g') # (Axe's, Data, width, color)
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
    plt.show()

draw_candle('TSLA', '10D')
