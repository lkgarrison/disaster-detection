from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


tweets = list(['This hurricane is going to be disasterous!', 'The hurricane is going to ruin everything', 'I cant wait for the hurricanes to win tonight'])
labels = list(['+', '+', '-'])


if __name__ == "__main__":
    classifier = MultinomialNB()
    count_vectorizer = CountVectorizer(min_df=1, ngram_range=(1, 2))

    # train
    counts = count_vectorizer.fit_transform(tweets)
    classifier.fit(counts, labels)

    # test
    test_tweets = ['This hurricane is going to hit us very soon', 'I cant wait for the hurricanes to lose tonight']
    test_counts = count_vectorizer.transform(test_tweets)
    results = classifier.predict(test_counts)
    for index, result in enumerate(results):
        print result, test_tweets[index]
