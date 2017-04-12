import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion

from transformers import LengthTransformer
from labeled_data import get_training_data


def remove_training_data_from_testing_data(training_tweets, tweets):
    pass


def test_classifier(tweets):
    print "Testing classifier on all labeled tweets"

    labeled_data = get_training_data()

    # based on the desired training size each round, calculate how many rounds
    # of accuracy testing are needed for 100% coverage of the test data
    train_size = 0.9
    num_loops_for_full_coverage = int(1.0 / (1.0 - train_size))

    random.seed()
    accuracy_sum = 0
    for i in xrange(num_loops_for_full_coverage):
        # generate a random state to make the splitting each round random
        rs = random.randint(1, 100)
        XTrain, XTest, yTrain, yTest = train_test_split(labeled_data.tweets, labeled_data.labels, train_size=train_size, random_state=rs)

        pipeline = Pipeline([
            ('features', FeatureUnion([
                ('counts', CountVectorizer(min_df=1, ngram_range=(1, 3))),
                ('tweet_length', LengthTransformer())
            ])),
            ('classifier', MultinomialNB())
        ])

        pipeline.fit(XTrain, yTrain)
        results = pipeline.predict(XTest)

        accuracy = accuracy_score(results, yTest)
        # print "Accuracy:", accuracy
        accuracy_sum += accuracy

    print "Classifier accuracy: %s%%" % (float(accuracy_sum) / num_loops_for_full_coverage * 100)


def classify(tweets):
    training_data = get_training_data()
    testing_tweets = map(lambda tweet: tweet.text, tweets)

    pipeline = Pipeline([
        ('features', FeatureUnion([
            ('counts', CountVectorizer(min_df=1, ngram_range=(1, 2))),
            ('tweet_length', LengthTransformer())
        ])),
        ('classifier', MultinomialNB())
    ])

    pipeline.fit(training_data.tweets, training_data.labels)
    results = pipeline.predict(testing_tweets)

    relevant_tweets = list()
    for index, result in enumerate(results):
        print result, testing_tweets[index]
        if result == "+":
            relevant_tweets.append(tweets[index])

    return relevant_tweets
