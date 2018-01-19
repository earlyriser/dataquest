## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

days = len(bikes['cnt'])
days_over_5k =len([elem for elem in bikes['cnt'] if elem > 5000])

prob_over_5000 = days_over_5k/days

print(days, days_more_5k, prob_over_5000)

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))

def get_combinations(N, k):
    numerator = math.factorial(N)
    denominator = math.factorial(k) * math.factorial(N - k)
    return numerator / denominator

def find_combination_probability(N, k, p, q):
    return (p**k)*(q**(N-k))

def get_combinations_probability(N,k,p,q):
    return get_combinations(N, k) * find_combination_probability(N, k, p, q)


for elem in outcome_counts:
    N=30
    k=elem
    p=.39
    q=1-p
    outcome_probs= [get_combinations_probability(30, i, .39, .61) for i in outcome_counts]
    
print( outcome_probs)

## 5. Plotting the distribution ##

import matplotlib.pyplot as plt

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)

dist = binom.pmf(outcome_counts,30,0.39)

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, dist)
plt.show()

## 8. Computing the mean of a probability distribution ##

dist_mean = 30*0.39

## 9. Computing the standard deviation ##

dist_stdev = (30*.39*(1-.39))**(1/2)

## 10. A different plot ##

import scipy
from scipy import linspace
from scipy.stats import binom

outcome_counts = linspace(0,10,11)
dist = binom.pmf(outcome_counts,10,0.39)

plt.bar(outcome_counts, dist)
plt.show()


outcome_counts = linspace(0,100,101)
dist = binom.pmf(outcome_counts,100,0.39)

plt.bar(outcome_counts, dist)
plt.show()

## 11. The normal distribution ##

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 12. Cumulative density function ##

outcome_counts = linspace(0,30,31)
outcome_probs = binom.cdf(outcome_counts,30,0.39)
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 14. Faster way to calculate likelihood ##

k = 16
N = 30
p = 0.39
left_16 = binom.cdf(k,N,p)
right_16 = 1-left_16