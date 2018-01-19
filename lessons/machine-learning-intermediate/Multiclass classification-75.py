## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")

unique_regions = cars["origin"].unique()

print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_years = pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)

cars.drop(['cylinders','year'], axis=1, inplace=True)

print(cars.columns)

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]

highest_train_row = int(cars.shape[0] * .70)
train = shuffled_cars.iloc[0:highest_train_row]
test = shuffled_cars.iloc[highest_train_row:]

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}
features =  ['cyl_3', 'cyl_4', 'cyl_5', 'cyl_6', 'cyl_8', 'year_70', 'year_71', 'year_72', 'year_73', 'year_74', 'year_75', 'year_76', 'year_77', 'year_78', 'year_79', 'year_80', 'year_81', 'year_82']

for origin in unique_origins:
    model = LogisticRegression()
    model.fit(train[features], train["origin"]==origin)
    models[origin]=model

## 5. Testing the models ##

#create dataframe with 1,2,3 cols
testing_probs = pd.DataFrame(columns=unique_origins)

print(testing_probs)
for origin in unique_origins:
    X_test = test[features]
    testing_probs[origin] = models[origin].predict_proba( X_test)[:,1]

    print(models[origin].predict_proba( X_test))

## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)