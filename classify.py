from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm


def classify(tweets):
    # split_index = int(0.3 * len(tweets))
    # training_tweets = [tweet.text for tweet in tweets[:split_index]]
    # testing_tweets = [tweet.text for tweet in tweets[split_index:]]
    training_tweets = [tweet.text for tweet in tweets[:200]]
    testing_tweets = [tweet.text for tweet in tweets[200:500]]

    # outliers_fraction = 0.25
    classifier = svm.OneClassSVM(kernel="rbf", gamma=0.1)

    vectorizer = CountVectorizer(min_df=1)
    X = vectorizer.fit_transform(training_tweets)

    classifier.fit(X)
    X_test = vectorizer.transform(testing_tweets)
    results = classifier.predict(X_test)

    for index, result in enumerate(results):
        print result, tweets[index].text


# outliers_fraction = 0.25
# classifier = svm.OneClassSVM(kernel="rbf", gamma=0.1)
# sample_of_tweets = list()
# sample_of_tweets.append('this is a hurricane tweet')
# sample_of_tweets.append('this is a earthquake tweet zzz zzz')
# sample_of_tweets.append('zzz')
# # sample_of_tweets.append('this is a flood tweet')
# # sample_of_tweets.append('this is a tornado tweet')
# # sample_of_tweets.append('horrible flooding in the area with high winds')
# vectorizer = CountVectorizer(min_df=1)
# X = vectorizer.fit_transform(sample_of_tweets)
# print X
# print
# print X.toarray()
#
# classifier.fit(X)
#
# test_tweets = list()
# test_tweets.append('this is a hurricane tweet')
# test_tweets.append('this is a hurricane tweet')
# test_tweets.append('this is a hurricane tweet')
# test_tweets.append('this is a hurricane tweet')
# test_tweets.append('there is a raging hurricane along the coast hurricane')
# test_tweets.append('bahh bahh black sheep')
#
# print
# X_test = vectorizer.transform(test_tweets)
# print X_test
# result = classifier.predict(X_test)
#
# print result