## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
print(avengers.head(5))

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

true_avengers = avengers[avengers['Year']>1960]
true_avengers['Year'].hist()

## 5. Consolidating Deaths ##

def clean_deaths(row):
    cols =['Death1','Death2','Death3','Death4','Death5']
    num_deaths = 0
    for c in cols:
        death = row[c]
        if pd.isnull(death) or death =='NO':
            continue
        else:
            num_deaths += 1
    return num_deaths

true_avengers['Deaths'] = true_avengers.apply( clean_deaths, axis=1 )

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()

true_avengers['New Calc']=true_avengers['Year'].apply(lambda x : 2015-x)

print(true_avengers['New Calc'].head)

joined_accuracy_count = len(true_avengers['New Calc']==true_avengers['Years since joining'])