import filter
import classify

import os
import sys
import argparse
from datetime import datetime
from dateutil import parser as dateparser


def plot(dataset_filename):
    filtered_tweets = filter.filter(dataset_filename)
    relevant_tweets = classify.classify(filtered_tweets)

    counts_per_time_unit = dict()
    for tweet in relevant_tweets:
        # get python date from the tweet time
        tweet_date = dateparser.parse(tweet.time)

        # get key to uniquely identify the date and hour
        key = tweet_date.strftime("%Y-%m-%d: %H")

        if key in counts_per_time_unit:
            counts_per_time_unit[key] += 1
        else:
            counts_per_time_unit[key] = 1

    dates = sorted(counts_per_time_unit.keys())

    if not os.path.exists('distributions'):
        os.makedirs('distributions')

    # get distribution filename from the data source's filename
    distribution_filename = dataset_filename.split('/')[len(dataset_filename.split('/')) - 1]

    # remove the previous file extension
    distribution_filename = distribution_filename.split('.')[0]
    f = open('distributions/' + distribution_filename + '.csv', 'w')
    for key in dates:
        f.write(str(key) + "," + str(counts_per_time_unit[key]) + "\n")

    print "Successfully generated file", 'distributions/' + distribution_filename + '.csv'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get data on distribution of relevant tweets')
    parser.add_argument("tweets", type=str, help="File containing tweets")

    args = parser.parse_args()

    if not os.path.isfile(args.tweets):
        print "Dataset does not exist:", args.tweets
        sys.exit(1)

    plot(args.tweets)
