import pandas as pd 
from pandas import DataFrame
from lambdata_robinhester.accuracy import accuracy_score
from lambdata_robinhester.train import train_val_test_split
from lambdata_robinhester.replace import dictionary_feature

a_list=pd.Series([2039, 4992, 8906, 12094])
b_list=pd.Series([2039,4000,8000,12098])



print(accuracy_score(a_list,b_list))

df=pd.read_csv('https://raw.githubusercontent.com/robinhester/youtube_build/master/Youtube.csv',encoding='utf-8')

print(df.head())

train,val,test=train_val_test_split(df)

print(train.head())
print(val.head())
print(test.head())

names_map = {'CA': 'California', 'CO': 'Colorado',
             'CT': 'Conneticut', 'DC': 'District of Columbia',
             'TX': 'Texas'}

city_names_map = {'ATL': 'Atlanta', 'KS Cty': 'Kansas City',
                  'ST. Louis': 'Saint Louis', 'NYC': 'New York City',
                  'L.A.': 'Los Angeles'}

states = DataFrame({'abbrev': ['CA', 'CO', 'CT',
                               'DC', 'TX']})

cities = DataFrame({'abbrev': ['ATL', 'KS Cty',
                                'ST. Louis', 'NYC', 'L.A.']})

print(dictionary_feature(df, names_map))

print(dictionary_feature(df2, city_names_map))