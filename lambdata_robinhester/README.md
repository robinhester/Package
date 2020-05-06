# Package
unit-3-Lambda

## Installation

```sh
pip install _____
```

## Usage
```py
import numpy as np
from lambdata_robinhester.accuracy import accuracy_score

print(accuracy_score(alist,blist))
```

```py
from sklearn.model_selection import train_test_split
from lambdata_robinhester.train import train_val_test_split
train,test,val = train_val_test_split(database)
```

## Accuracy Score Function

```
Returns accuracy of a predicted value vs an
actual value

Params: x must equal an actual value, y must
equal a predicted value, values can be in either panda
series or dataframe form

Example: a_list=pd.Series([2039, 4992, 8906, 12094])
b_list=pd.Series([2039,4000,8000,12098])

Returns: percent of correct values vs incorrect values
for comparison
```

## Train Test Val Split Function

```
Does a train, test, validation three way
split for predictive modeling

Params: a database for predictive models.

Example: csv file loaded in from pandas.
Must be inputed as: train, test, val = train_val_test_split(database)

Returns: three seperate databases ready for
predictive models and to be split into target and features
```

## Required Packages

```sh
Pandas
Numpy
Sklearn
Sklearn.model_selction(train_test_split)
```
