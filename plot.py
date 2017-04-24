import filter
import classify
from datetime import datetime
import argparse
from dateutil import parser as dateparser


def plot(data):
    filtered_tweets = filter.filter(data)
    relevant_tweets = classify.classify(filtered_tweets)
    counts_per_time_unit = dict()
    for tweet in relevant_tweets:
        # get python date from the tweet time
        tweet_date = dateparser.parse(tweet.time)

        # create key to uniquely identify the date
        key = ' '.join(map(str, [tweet_date.year, tweet_date.month, tweet_date.day]))

        # add the hour window to the key
        key += ' ' + str(tweet_date.hour)

        # hour=int(time_hms[0])
        # if hour < 1:
        # 	key += " 00"
        # elif hour < 16:
        # 	key+=" 08"
        # else:
        # 	key += " 12"

        # key += " " + str(hour)

        if key in counts_per_time_unit:
            counts_per_time_unit[key] += 1
        else:
            counts_per_time_unit[key] = 1

    dates = sorted(counts_per_time_unit.keys())
    f = open("distributions/tmp.csv", "w")
    for key in dates:
        f.write(str(key) + "," + str(counts_per_time_unit[key]) + "\n")


def getDateFromKey(key):
    # return datetime.strptime(key, "%d %b %Y %p")
    return datetime.strptime(key, "%d %b %Y %H")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get data on distribution of relevant tweets')
    parser.add_argument("tweets", type=str, help="File containing tweets")

    args = parser.parse_args()
    plot(args.tweets)
