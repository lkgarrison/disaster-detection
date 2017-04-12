from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


class DataFrame:
    """ a container to hold tweets and their labels
        the text at a given index is always matched with the label at the same index
    """
    def __init__(self):
        self.tweets = list()
        self.labels = list()
        self._possible_labels = ['+', '-']

    def add_labeled_tweet(self, tweet, label):
        if label not in self._possible_labels:
            print "Error: invalid label:", label
            print "\tTweet:", tweet
        else:
            self.tweets.append(tweet)
            self.labels.append(label)


def remove_training_data_from_testing_data(training_tweets, tweets):
    pass


def classify(tweets):
    training_data = get_training_data()
    testing_tweets = [tweet.text for tweet in tweets[101:155]]

    classifier = MultinomialNB()
    count_vectorizer = CountVectorizer(min_df=1, ngram_range=(1, 2))

    # train
    counts = count_vectorizer.fit_transform(training_data.tweets)
    classifier.fit(counts, training_data.labels)

    # test
    testing_counts = count_vectorizer.transform(testing_tweets)
    results = classifier.predict(testing_counts)

    relevant_tweets = list()
    for index, result in enumerate(results):
        print result, tweets[101 + index].text
        if result == "+":
            relevant_tweets.append(tweets[index])

    return relevant_tweets


# get a list of the training tweets from the training file
def get_training_data():
    count = 0

    # the number of approved hurricane example tweets
    max_count = 100
    with open("training_data.txt") as f:
        data = DataFrame()

        for line in f:
            line = line.rstrip()
            if len(line) == 0:
                raise "Error: line %s is a blank line" % (count + 1)

            label = line[0]
            tweet = line[1:]

            data.add_labeled_tweet(tweet, label)

            count += 1

            if count >= max_count:
                return data

        return data
