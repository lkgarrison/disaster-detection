import re
from sklearn.base import TransformerMixin

from keywords import disaster_keywords


# Custom feature that returns the number of words in each tweet
class LengthTransformer(TransformerMixin):

    def transform(self, X, **transform_params):
        results = list()
        for tweet in X:
            results.append([len(tweet.split(' '))])
        return results

    def fit(self, X, y=None, **fit_params):
        return self


class KeywordWeightsTransformer(TransformerMixin):
    def __init__(self, disaster_type):
        self.disaster_type = disaster_type

    def transform(self, X, **transform_params):
        results = list()
        for tweet in X:
            keyword_sum = 0.0
            keyword_weights = disaster_keywords[self.disaster_type]
            keyword_regex = dict()
            for keyword in keyword_weights:
                keyword_regex[keyword] = re.compile(r'\b%s\b' % (keyword), re.IGNORECASE)

            for keyword in keyword_regex:
                if keyword_regex[keyword].findall(tweet):
                    keyword_sum += keyword_weights[keyword]

            results.append([keyword_sum])
            # print keyword_sum, tweet
        # print results
        return results

    def fit(self, X, y=None, **fit_params):
        return self
