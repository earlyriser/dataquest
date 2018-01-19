## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig = plt.figure(figsize=(5,12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)
ax4.set_xlim(0,5.0)
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)

ax1.hist(movie_reviews['RT_user_norm'])
ax2.hist(movie_reviews['Metacritic_user_nom'])
ax3.hist(movie_reviews['Fandango_Ratingvalue'])
ax4.hist(movie_reviews['IMDB_norm'])

## 2. Mean ##

def calc_mean(series):
    vals = series.values
    return sum(vals)/len(vals)

user_reviews = movie_reviews[['RT_user_norm','Metacritic_user_nom','Fandango_Ratingvalue','IMDB_norm']]


rt_mean=user_reviews.apply(calc_mean)['RT_user_norm']
mc_mean=user_reviews.apply(calc_mean)['Metacritic_user_nom']
fg_mean=user_reviews.apply(calc_mean)['Fandango_Ratingvalue']
id_mean=user_reviews.apply(calc_mean)['IMDB_norm']

## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_std(series):
    return calc_variance(series)**(1/2)


user_reviews = movie_reviews[['RT_user_norm','Metacritic_user_nom','Fandango_Ratingvalue','IMDB_norm']]


rt_var=user_reviews.apply(calc_variance)['RT_user_norm']
rt_stdev=user_reviews.apply(calc_std)['RT_user_norm']

mc_var=user_reviews.apply(calc_variance)['Metacritic_user_nom']
mc_stdev=user_reviews.apply(calc_std)['Metacritic_user_nom']

fg_var=user_reviews.apply(calc_variance)['Fandango_Ratingvalue']
fg_stdev=user_reviews.apply(calc_std)['Fandango_Ratingvalue']

id_var=user_reviews.apply(calc_variance)['IMDB_norm']
id_stdev=user_reviews.apply(calc_std)['IMDB_norm']

## 4. Scatter plots ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4,8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)

ax1.scatter(user_reviews["RT_user_norm"], user_reviews["Fandango_Ratingvalue"])
ax2.scatter(user_reviews["Metacritic_user_nom"], user_reviews["Fandango_Ratingvalue"])
ax3.scatter(user_reviews["IMDB_norm"], user_reviews["Fandango_Ratingvalue"])


## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean


def calc_covariance(x,y): 
    x_mean = calc_mean(x)
    y_mean = calc_mean(y)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)  

rt_fg_covar = calc_covariance(user_reviews['RT_user_norm'], user_reviews['Fandango_Ratingvalue'])
mc_fg_covar = calc_covariance(user_reviews['Metacritic_user_nom'], user_reviews['Fandango_Ratingvalue'])
id_fg_covar = calc_covariance(user_reviews['IMDB_norm'], user_reviews['Fandango_Ratingvalue'])

## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

def calc_correlation(series_one, series_two):
    numerator = calc_covariance(series_one, series_two)
    series_one_std = calc_variance(series_one) ** (1/2)
    series_two_std = calc_variance(series_two) ** (1/2)
    denominator = series_one_std * series_two_std
    correlation = numerator / denominator
    return correlation

rt_fg_covar = calc_covariance(user_reviews["RT_user_norm"], user_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(user_reviews["Metacritic_user_nom"], user_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(user_reviews["IMDB_norm"], user_reviews["Fandango_Ratingvalue"])


rt_fg_corr = calc_correlation(user_reviews["RT_user_norm"], user_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(user_reviews["Metacritic_user_nom"], user_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(user_reviews["IMDB_norm"], user_reviews["Fandango_Ratingvalue"])

print("Correlation between Rotten Tomatoes and Fandango", rt_fg_corr)
print("Correlation between Metacritic and Fandango", mc_fg_corr)
print("Correlation between IMDB and Fandango", id_fg_corr)