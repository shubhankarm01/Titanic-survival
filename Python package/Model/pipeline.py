from sklearn.pipeline import Pipeline


from feature_engine.encoding import RareLabelEncoder, OneHotEncoder
from feature_engine.imputation import CategoricalImputer, AddMissingIndicator, MeanMedianImputer
from Model.Processing.features import ExtractLetterTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from Model.Config.core import config

titanic_pipe = Pipeline([

    # ===== IMPUTATION =====
    # impute categorical variables with string 'missing'
    ('categorical_imputation', CategoricalImputer(imputation_method = 'missing', 
                                                  variables = config.model_config.categorical_vars)),

    # add missing indicator to numerical variables
    ('missing_indicator', AddMissingIndicator(variables  = config.model_config.numerical_vars)),

    # impute numerical variables with the median
    ('median_imputation', MeanMedianImputer(imputation_method = 'median',
                                            variables = config.model_config.numerical_vars)),


    # Extract first letter from cabin
    ('extract_letter', ExtractLetterTransformer(variables = config.model_config.cabin_vars)),


    # == CATEGORICAL ENCODING ======
    # remove categories present in less than 5% of the observations (0.05)
    # group them in one category called 'Rare'
    ('rare_label_encoder', RareLabelEncoder(tol = 0.05,
                                            n_categories = 1, 
                                            variables = config.model_config.categorical_vars)),


    # encode categorical variables using one hot encoding into k-1 variables
    ('categorical_encoder', OneHotEncoder(drop_last = True, 
                                          variables = config.model_config.categorical_vars)),

    # scale using standardization
    ('scaler', StandardScaler()),
#     ('scaler', num_scaling(variables = NUMERICAL_VARIABLES)),

    # logistic regression (use C=0.0005 and random_state=0)
    ('Logit', LogisticRegression(C = 0.0005, random_state = 0)),
])