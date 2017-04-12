from sklearn.base import TransformerMixin


# Custom feature that returns the number of words in each tweet
class LengthTransformer(TransformerMixin):

    def transform(self, X, **transform_params):
        results = list()
        for tweet in X:
            results.append([len(tweet.split(' '))])
        return results

    def fit(self, X, y=None, **fit_params):
        return self
