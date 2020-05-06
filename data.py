import pandas as pd 
from lambdata_robinhester.accuracy import accuracy_score
from lambdata_robinhester.train import train_val_test_split

a_list=pd.Series([2039, 4992, 8906, 12094])
b_list=pd.Series([2039,4000,8000,12098])



print(accuracy_score(a_list,b_list))

df=pd.read_csv('https://raw.githubusercontent.com/robinhester/youtube_build/master/Youtube.csv',encoding='utf-8')

print(df.head())

train,val,test=train_val_test_split(df)

print(train.head())
print(val.head())
print(test.head())
