import configparser
from data_sources.Quandl import Quandl
from nltk.tokenize import word_tokenize
from utils.DataCleaner import DataCleaner
from utils.SentimentAnalysis import SentimentAnalysis
from data_sources.social_media.Twitter import Twitter

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config/config.ini')

    quandl = Quandl(config['quandl']['api_key'])
    btc_price_data = quandl.getBitcoinPriceData()

    twitter = Twitter(config['twitter']['api_key'], config['twitter']['api_secret'], 1, 1)
    twitter.getBearerToken()
    tweets = twitter.getTweets()

    s = SentimentAnalysis()
    for tweet in tweets:
        tokens = DataCleaner.remove_noise_from_text(word_tokenize(tweet['text']))
        #print(tweet['text'], s.classifyTokens(tokens))