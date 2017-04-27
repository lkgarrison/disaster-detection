from collections import Counter
from dateutil import parser as dateparser

# The probabilistic model
# Returns true/false if there is a disaster occurring. If true, returns the
# hour the disaster was detected as well

TWEET_PER_HOUR_THRESHOLD = 175


def predict(relevant_tweets):
    # use plot.py code here to determine if there there is an hour
    counts_per_time_unit = Counter()

    for tweet in relevant_tweets:
        # get python date from the tweet time
        tweet_date = dateparser.parse(tweet.time)

        key = tweet_date.strftime("%Y-%m-%d: %H")

        counts_per_time_unit[key] += 1

    dates = sorted(counts_per_time_unit.keys())

    for key in dates:
        if counts_per_time_unit[key] > TWEET_PER_HOUR_THRESHOLD:
            print "Hurricane detected at:", key
            print "Hurricane tweets started in the hour:", key
            return

    print "No disaster detected"
