import ast
import re
import string
import os
import sys


class Tweet(object):
    def __init__(self, text, time, geo):
        self.text = text
        self.time = time
        self.geo = geo


def filter(dataset):
    count = 0
    hurricane_re = re.compile(r'\bhurricane\b|\bflood\b|\brain\b', re.IGNORECASE)
    training_file_name = 'training_data.txt'
    # don't accidentally overwrite the training file if it was already written
    if os.path.isfile(training_file_name):
        print "training file already exists:", training_file_name
        sys.exit(1)
    else:
        outfile = open(training_file_name, "w")

    num_tweets_with_errors = 0
    for line in open(dataset, 'r'):
        try:
            tweetdict = ast.literal_eval(line)
            if hurricane_re.findall(tweetdict['text']):
                tweet = ''.join([c for c in tweetdict['text'] if c in string.printable])
                tweet = tweet.replace('\n', ' ')
                outfile.write(tweet + '\n')

        except SyntaxError:
            num_tweets_with_errors += 1

        if count > 2000:
            print "Training tweets are now located in:", training_file_name
            return

        count += 1


if __name__ == "__main__":
    filter("data/sandy_hurricane.txt")
