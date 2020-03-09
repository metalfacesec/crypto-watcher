import quandl
import pandas
from os import path

class Quandl:
    def __init__(self, api_key):
        self.btc_data_file_path = './data/bitcoin_usd.csv'
        self.api_key = api_key
        self.setApiKey(self.api_key)

    def shouldGetBitcoinDataFromAPI(self):
        return not path.exists(self.btc_data_file_path)

    def setApiKey(self, key):
        quandl.ApiConfig.api_key = key

    def getBitcoinPriceData(self):
        if self.shouldGetBitcoinDataFromAPI():
            btc_price_data = self.getBitcoinPricesFromAPI()
            self.saveDataToCSV(btc_price_data)
            return btc_price_data
        return self.getBitcoinPricesFromCSV()
        

    def getBitcoinPricesFromAPI(self):
        print('gettting from api')
        return quandl.get("BITSTAMP/USD")

    def getBitcoinPricesFromCSV(self):
        print('getting from csv')
        return self.getDataFromCSV()

    def saveDataToCSV(self, dataFrame):
        dataFrame.to_csv(self.btc_data_file_path)

    def getDataFromCSV(self):
        return pandas.read_csv(self.btc_data_file_path, parse_dates=['Date'])