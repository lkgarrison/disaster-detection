NUM_LABELED_TWEETS = 730


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


# get a list of the training tweets from the training file
def get_training_data():
    count = 0

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

            if count >= NUM_LABELED_TWEETS:
                return data

        return data
