import nltk
import random
from .DataCleaner import DataCleaner
from nltk.corpus import twitter_samples, stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier

class SentimentAnalysis:
    def __init__(self):
        self.classifier = None
        self.trainModelTwitterData()

    def classifyTokens(self, tokens):
        return self.classifier.classify(dict([token, True] for token in tokens))

    def get_tweets_for_model(self, cleaned_tokens_list):
        for tweet_tokens in cleaned_tokens_list:
            yield dict([token, True] for token in tweet_tokens)

    def trainModelTwitterData(self):
        stop_words = stopwords.words('english')

        positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
        negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

        positive_cleaned_tokens_list = []
        for tokens in positive_tweet_tokens:
            positive_cleaned_tokens_list.append(DataCleaner.remove_noise_from_text(tokens, stop_words))


        negative_cleaned_tokens_list = []
        for tokens in negative_tweet_tokens:
            negative_cleaned_tokens_list.append(DataCleaner.remove_noise_from_text(tokens, stop_words))

        positive_tokens_for_model = self.get_tweets_for_model(positive_cleaned_tokens_list)
        negative_tokens_for_model = self.get_tweets_for_model(negative_cleaned_tokens_list)

        positive_dataset = [(tweet_dict, "Positive") for tweet_dict in positive_tokens_for_model]
        negative_dataset = [(tweet_dict, "Negative") for tweet_dict in negative_tokens_for_model]

        dataset = positive_dataset + negative_dataset

        random.shuffle(dataset)

        train_data = dataset[:7000]
        test_data = dataset[7000:]

        self.classifier = NaiveBayesClassifier.train(train_data)
