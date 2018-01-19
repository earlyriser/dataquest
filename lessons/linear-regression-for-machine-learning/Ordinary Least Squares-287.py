## 1. Introduction ##

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

features = ['Wood Deck SF', 'Fireplaces', 'Full Bath', '1st Flr SF', 'Garage Area',
       'Gr Liv Area', 'Overall Qual']

X = train[features]
y = train["SalePrice"]

xt = np.transpose(X)
x_by_xt = np.dot(xt, X)
inverse_x_xt = np.linalg.inv( x_by_xt)
xt_y = np.dot(xt, y)
a = np.dot(inverse_x_xt, xt_y)