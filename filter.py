import ast
import re
import string
import json

from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

from labeled_data import get_training_data
from keywords import disaster_keywords

class Tweet(object):
    def __init__(self, text, time, geo):
        self.text = text
        self.time = time
        self.geo = geo


def filter(dataset):
    training_tweets = set(get_training_data().tweets)

    filtered_tweets = []

    # build up disaster regular expression based on the defined keywords
    hurricane_re_str = str()
    for index, keyword in enumerate(disaster_keywords['hurricane']):
        hurricane_re_str += '\\b' + keyword + '\\b'

        # add the "or" regex unless it is the last keyword for the disaster
        if index != len(disaster_keywords['hurricane']) - 1:
            hurricane_re_str += '|'

    hurricane_re = re.compile(r'%s' % (hurricane_re_str), re.IGNORECASE)

    count = 0
    num_tweets_with_errors = 0
    for line in open(dataset, 'r'):
        try:
            # try reading in the file two different ways depending on the json format
            try:
                tweetdict = ast.literal_eval(line)
            except ValueError:
                try:
                    tweetdict = json.loads(line)
                except ValueError as e:
                    raise e

            tweet_text = tweetdict['text'].replace('\n', ' ')

            if hurricane_re.findall(tweet_text):
                # ensure the model isn't biased by including tweets from the training data in the test data set
                if tweet_text not in training_tweets:
                    # ensure the tweet contains only printable characters
                    tweet_text = ''.join([c for c in tweet_text if c in string.printable])
                    filtered_tweets.append(Tweet(tweet_text, tweetdict['created_at'], tweetdict['geo']))
                    count += 1

        except SyntaxError:
            num_tweets_with_errors += 1

        # if count >= 400:
            # break

    print "finished reading in tweets"

    if num_tweets_with_errors > 0:
        print "Number of tweets unable to be parsed:", num_tweets_with_errors

    print 'number of hurricane tweets:', len(filtered_tweets)

    return filtered_tweets


if __name__ == "__main__":
    # filter("data/hurricane-tweets.txt")
    filter("data/irene_hurricane.txt")
