import ast
import re
import string

from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

class Tweet(object):
    def __init__(self, text, time, geo):
        self.text = text
        self.time = time
        self.geo = geo


def filter(dataset):
    tweets = []
    hurricane_re = re.compile(r'\bhurricane\b|\bflood\b|\brain\b', re.IGNORECASE)

    num_tweets_with_errors = 0
    for line in open(dataset, 'r'):
        try:
            tweetdict = ast.literal_eval(line)
            if hurricane_re.findall(tweetdict['text']):
                # ensure the tweet contains only printable characters
                tweet_text = ''.join([c for c in tweetdict['text'] if c in string.printable])
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
