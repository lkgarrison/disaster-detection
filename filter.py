import ast
import re


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
                tweets.append(Tweet(tweetdict['text'], tweetdict['created_at'], tweetdict['geo']))

        except SyntaxError:
            num_tweets_with_errors += 1

    print "finished reading in tweets"

    if num_tweets_with_errors > 0:
        print "Number of tweets unable to be parsed:", num_tweets_with_errors

    print 'number of hurricane tweets:', len(tweets)

if __name__ == "__main__":
    filter("data/irene_hurricane.txt")
