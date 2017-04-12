import ast
import re
import string

from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

from labeled_data import get_training_data

class Tweet(object):
    def __init__(self, text, time, geo):
        self.text = text
        self.time = time
        self.geo = geo


def filter(dataset):
    training_tweets = set(get_training_data().tweets)

    tweets = []
    hurricane_re = re.compile(r'\bhurricane\b|\bflood\b|\brain\b', re.IGNORECASE)

    num_tweets_with_errors = 0
    for line in open(dataset, 'r'):
        try:
            tweetdict = ast.literal_eval(line)
            tweet_text = tweetdict['text']
            if hurricane_re.findall(tweet_text):
                # ensure the model isn't biased by including tweets from the training data in the test data set
                if tweet_text not in training_tweets:
                    # ensure the tweet contains only printable characters
                    tweet_text = ''.join([c for c in tweet_text if c in string.printable])
                    tweets.append(Tweet(tweet_text, tweetdict['created_at'], tweetdict['geo']))

        except SyntaxError:
            num_tweets_with_errors += 1

    print "finished reading in tweets"

    if num_tweets_with_errors > 0:
        print "Number of tweets unable to be parsed:", num_tweets_with_errors

    print 'number of hurricane tweets:', len(tweets)

    return tweets


if __name__ == "__main__":
    filter("data/irene_hurricane.txt")
