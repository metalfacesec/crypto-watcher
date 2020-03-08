import configparser
from nltk.tokenize import word_tokenize
from utils.DataCleaner import DataCleaner
from utils.SentimentAnalysis import SentimentAnalysis
from data_sources.social_media.Twitter import Twitter

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config/config.ini')

    t = Twitter(config['twitter']['api_key'], config['twitter']['api_secret'], 1, 1)
    t.getBearerToken()
    tweets = t.getTweets()

    s = SentimentAnalysis()
    for tweet in tweets:
        tokens = DataCleaner.remove_noise_from_text(word_tokenize(tweet['text']))
        print(tweet['text'], s.classifyTokens(tokens))



#bitcoinPriceData = getDataFromCSV('./bitcoin_usd.csv')

#bitcoinPriceData['5_day_MA'] = bitcoinPriceData['Last'].rolling(5).sum()

#print(bitcoinPriceData)
#bitcoinPriceData.set_index('Date',inplace=True)
# bitcoinPriceData['Volume'].plot()
# bitcoinPriceData['Low'].plot()

# plt.plot(bitcoinPriceData['5_day_MA'])
# plt.title('5 Day Moving Average')
# plt.show()

# bitcoinPriceData = getBitcoinPriceData()
# saveDataToCSV(bitcoinPriceData)