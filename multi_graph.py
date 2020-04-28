import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
import os
import shutil

companies_to_plot = ['AAPL','MSFT', 'NFLX' ]

start = dt.datetime(2019,6,1)
end = dt.datetime.now()


def clean_directory(path):

    # This method removes all the files in the "stock_dfs" directory.

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def get_data(tick):
    df = web.DataReader(tick, 'yahoo', start, end)  # Get info from Yahoo
    df.to_csv('stock_dfs/' + str(tick) + '.csv')  # Create .csv


def compare_companies(companies_to_plot, start_date, end_date, column):

    style.use('Solarize_Light2')

    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)  # (Grid size, Starting point, rowspan, colspan)
    plt.title(companies_to_plot)  # Title
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
    plt.title('Volume')

    for company in companies_to_plot:

        get_data(company)

        df = pd.read_csv('stock_dfs/' + str(company) + '.csv', parse_dates=True, index_col=0)  # Read data from .csv
        df['100ma'] = df['Adj Close'].rolling(window=100).mean()  # Create a new column for 100 moving average

        ax1.plot(df.index, df[column])  # (x, y)
        ax2.plot(df.index, df["Volume"])  # (x, y)

        ax1.legend(companies_to_plot, loc='upper left', borderaxespad=0.)

    plt.show()


clean_directory("stock_dfs")
compare_companies(companies_to_plot, start, end, "High")