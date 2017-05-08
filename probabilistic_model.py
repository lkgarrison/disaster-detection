from collections import Counter
from dateutil import parser as dateparser

# The probabilistic model
# Returns true/false if there is a disaster occurring. If true, returns the
# hour the disaster was detected as well

TWEET_PER_HOUR_THRESHOLD = 200


def predict(relevant_tweets):
    # use plot.py code here to determine if there there is an hour
    counts_per_time_unit = Counter()

    # sort the tweets by time
    relevant_tweets.sort(key=lambda tweet: dateparser.parse(tweet.time).isoformat())

    # traverse tweets in chronological order
    for tweet in relevant_tweets:
        # get python date from the tweet time
        tweet_date = dateparser.parse(tweet.time)

        key = tweet_date.strftime("%Y-%m-%d: %H")

        counts_per_time_unit[key] += 1

        if counts_per_time_unit[key] > TWEET_PER_HOUR_THRESHOLD:
            datediff = dateparser.parse(tweet.time) - dateparser.parse(relevant_tweets[0].time)
            print "Hurricane detected at:", tweet.time
            print "Hurricane tweets started at:", relevant_tweets[0].time
            print "Hurricane detected in", get_time_diff(datediff)
            return

    print "No disaster detected"


# return a string containing the number of das, hours, min, sec of the
# given datetime.diff object
def get_time_diff(duration):
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)

    duration_str = str()
    if days > 0:
        duration_str += "{} day{} ".format(days, 's' if days != 1 else '')
    if hours > 0:
        duration_str += "{} hour{} ".format(hours, 's' if hours != 1 else '')
    if minutes > 0:
        duration_str += "{} minute{} ".format(minutes, 's' if minutes != 1 else '')
    if seconds > 0:
        duration_str += "{} second{} ".format(seconds, 's' if seconds != 1 else '')

    return duration_str
