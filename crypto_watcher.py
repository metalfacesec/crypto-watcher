import quandl
import pandas
import matplotlib.pyplot as plt

def setQuandlAPIKey(key):
    quandl.ApiConfig.api_key = key

def getBitcoinPriceData():
    return quandl.get("BITSTAMP/USD")

def saveDataToCSV(dataFrame):
    dataFrame.to_csv('./bitcoin_usd.csv')

def getDataFromCSV(csv_path):
    return pandas.read_csv(csv_path, parse_dates=['Date'])

def main():
    bitcoinPriceData = getDataFromCSV('./bitcoin_usd.csv')

    bitcoinPriceData['5_day_MA'] = bitcoinPriceData['Last'].rolling(5).sum()

    print(bitcoinPriceData)
    bitcoinPriceData.set_index('Date',inplace=True)
    bitcoinPriceData['Volume'].plot()
    bitcoinPriceData['Low'].plot()

    # plt.plot(bitcoinPriceData['5_day_MA'])
    # plt.title('5 Day Moving Average')
    plt.show()
    # setQuandlAPIKey('XXXXXX')

    # bitcoinPriceData = getBitcoinPriceData()
    # saveDataToCSV(bitcoinPriceData)

if __name__ == '__main__':
    main()