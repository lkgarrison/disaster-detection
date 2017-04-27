import re
from sklearn.base import TransformerMixin

from keywords import disaster_keywords


def get_keyword_regex_dict(disaster_type):
    keyword_regex = dict()

    for keyword in disaster_keywords[disaster_type]:
        keyword_regex[keyword] = re.compile(r'\b%s\b' % (keyword), re.IGNORECASE)

    return keyword_regex


# Custom feature that returns the number of words in each tweet
class LengthTransformer(TransformerMixin):

    def transform(self, X, **transform_params):
        results = list()
        for tweet in X:
            results.append([len(tweet.split(' '))])
        return results

    def fit(self, X, y=None, **fit_params):
        return self


# Custom feature that returns the position of the keyword in each tweet
class KeywordPositionTransformer(TransformerMixin):
    def __init__(self, disaster_type):
        self.disaster_type = disaster_type

    def transform(self, X, **transform_params):
        results = list()
        disaster_keyword_weights = disaster_keywords[self.disaster_type]

        for tweet in X:
            indices = list()
            found_keyword = False
            keyword_regex = get_keyword_regex_dict(self.disaster_type)

            # try the highest weighted keywords first
            for keyword in sorted(disaster_keyword_weights, key=disaster_keyword_weights.get, reverse=True):
                for index, word in enumerate(tweet.split(' ')):
                    if keyword_regex[keyword].findall(word):
                        indices.append(index)
                        found_keyword = True
                        break

                if found_keyword:
                    break

            if not found_keyword:
                # a sentinel value that indicates the keywords were not found
                indices = [999]

            results.append(indices)

        return results

    def fit(self, X, y=None, **fit_params):
        return self


# custom feature that returns the sum of the weights of the keywords in the tweet
class KeywordWeightsTransformer(TransformerMixin):
    def __init__(self, disaster_type):
        self.disaster_type = disaster_type

    def transform(self, X, **transform_params):
        results = list()
        for tweet in X:
            keyword_sum = 0.0
            keyword_weights = disaster_keywords[self.disaster_type]
            keyword_regex = get_keyword_regex_dict(self.disaster_type)

            for keyword in keyword_regex:
                if keyword_regex[keyword].findall(tweet):
                    keyword_sum += keyword_weights[keyword]

            results.append([keyword_sum])

        return results

    def fit(self, X, y=None, **fit_params):
        return self
