# TASK 1

# Import all required libraries
import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt

"""
1. Using any finance API (we use Yahoo Finance and Tiingo during sessions) download historical stock prices for Google
(symbol 'GOOG'), for the period 1 Jan 2020 to 1 Jan 2021
"""

api_token = '1c0af2df7ce543a90a6d13c2b6b4f87a659f496b'

startDate = '2020-01-01'
endDate = '2021-01-01'

dataframe = pdr.tiingo.TiingoDailyReader('GOOG', start=startDate, end = endDate, api_key=api_token)

google_stock_df = dataframe.read()
# print(google_stock_df)


"""
2. Save these prices to csv file with Pandas
"""

google_csv = google_stock_df.to_csv('google_stock_prices_2020', date_format='%Y-%m-%d')

"""
3. Read this csv file to display data saved
"""

saved_csv = pd.read_csv('google_stock_prices_2020', header=0, index_col='date', parse_dates=True)
# print(saved_csv)

"""
4. Plot a simple diagram to display closing prices for GOOG stock
"""
plt.figure(1)
plt.plot(saved_csv['close'])
plt.title('Closing Stock Price of Google in 2020')
plt.xlabel('Date')
plt.ylabel('Closing Stock Price (USD)')
plt.grid()



# TASK 2

"""
Repeat exactly the same steps and plot a similar diagram for Microsoft stock.
"""

dataframe = pdr.tiingo.TiingoDailyReader('MSFT', start=startDate, end = endDate, api_key=api_token)

microsoft_stock_df = dataframe.read()
# print(google_stock_df)
microsoft_csv = microsoft_stock_df.to_csv('microsoft_stock_prices_2020', date_format='%Y-%m-%d')

microsoft_csv_saved = pd.read_csv('microsoft_stock_prices_2020', header=0, index_col='date', parse_dates=True)
# print(microsoft_csv_saved)

plt.figure(2)
plt.plot(microsoft_csv_saved['close'])
plt.title('Closing Stock Price of Microsoft in 2020')
plt.xlabel('Date')
plt.ylabel('Closing Stock Price (USD)')
plt.grid()
plt.show()
