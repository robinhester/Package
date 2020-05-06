import sklearn
from sklearn.model_selection import train_test_split


def train_val_test_split(X):
    """
    Does a train, test, validation three way
    split for predictive modeling

    Params: a database for predictive models.

    Example: csv file loaded in from pandas.
    Must be inputed as:
    train, test, val = train_val_test_split(database)

    Returns: three seperate databases ready for
    predictive models and to be split into target and features
    """
    train = X.copy()
    train, test = train_test_split(train, train_size=.80, test_size=.20,
                                   random_state=42)

    train, val = train_test_split(train, test_size=.20,
                                  random_state=42)

    return(train, test, val)
