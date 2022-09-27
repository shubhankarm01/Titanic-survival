from sklearn.base import BaseEstimator, TransformerMixin

class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variables):
        self.variables = variables

    def fit(self, x, y = None):
        return self

    def transform(self, x):
        x = x.copy()
        
        x[self.variables[0]] = x[self.variables[0]].str[0]

        return x