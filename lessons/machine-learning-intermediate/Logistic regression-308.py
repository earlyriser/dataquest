## 2. Introduction to the data ##

['import pandas as pd\nimport matplotlib.pyplot as plt\n\nadmissions = pd.read_csv("admissions.csv")\n\nplt.scatter(x=admissions[\'gpa\'], y=admissions[\'admit\'])\nplt.show()']

## 4. Logistic function ##

import numpy as np

# Logistic Function
def logistic(x):
    # np.exp(x) raises x to the exponential power, ie e^x. e ~= 2.71828
    return np.exp(x)  / (1 + np.exp(x)) 
    
# Generate 50 real values, evenly spaced, between -6 and 6.
x = np.linspace(-6,6,50, dtype=float)

# Transform each number in t using the logistic function.
y = logistic(x)

# Plot the resulting data.
plt.plot(x, y)
plt.ylabel("Probability")
plt.show()

## 5. Training a logistic regression model ##

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

linear_model = LinearRegression()
linear_model.fit(admissions[["gpa"]], admissions["admit"])

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])

## 6. Plotting probabilities ##

import matplotlib.pyplot as plt

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])

pred_probs = logistic_model.predict_proba(admissions[["gpa"]])
# Probability that the row belongs to label `0`.
pred_probs[:,0]
# Probabililty that the row belongs to label `1`.
pred_probs[:,1]

plt.scatter(x=admissions['gpa'], y=pred_probs[:,1])
plt.show()

## 7. Predict labels ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])

fitted_labels = logistic_model.predict(admissions[["gpa"]])

print(fitted_labels[0:10])

plt.scatter(admissions["gpa"], fitted_labels)
plt.xlabel("GPA")
plt.ylabel("Admit")