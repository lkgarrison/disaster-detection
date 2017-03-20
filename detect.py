import filter
import classify

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Uses Twitter data to determine if there is a disaster or not')
    parser.add_argument("tweets", type=str, help="Tweets to use to detect if a disaster has occured")

    args = parser.parse_args()

    filtered_tweets = filter.filter(args.tweets)
    classify.classify(filtered_tweets)