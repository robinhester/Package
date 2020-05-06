import numpy as np


def accuracy_score(x, y):
    """
    Returns accuracy of a predicted value vs an
    actual value

    Params: x must equal an actual value, y must
    equal a predicted value, values can be in either panda
    series or dataframe form

    Example: a_list=pd.Series([2039, 4992, 8906, 12094])
             b_list=pd.Series([2039,4000,8000,12098])

    Returns: percent of correct values vs incorrect values
    for comparison
    """
    errors = abs(y - x)
    accuracy_mean = np.mean(100 * (errors / x))
    accuracy = 100 - accuracy_mean

    return(accuracy)
