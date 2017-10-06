import pandas
import math
import matplotlib.pyplot as plt


bikes = pandas.read_csv("bike_rental_day.csv")

#get probablity of days with more of 5000 bike uses
days = len(bikes['cnt'])
days_over_5k =len([elem for elem in bikes['cnt'] if elem > 5000])
prob_over_5000 = days_over_5k/days
print("days", days)
print("days_over_5k", days_over_5k)
print("prob_over_5000", prob_over_5000)


#compute a distribution of the probability of 0 days with over 5000 to 30 days over 5000 
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
    p=prob_over_5000
    q=1-p
    outcome_probs= [get_combinations_probability(30, i, .39, .61) for i in outcome_counts]


#plot the distribution
plt.bar(outcome_counts, outcome_probs)
plt.show()


#we can simplify the distribution computation with scipy binom
import scipy
from scipy import linspace
from scipy.stats import binom

outcome_counts = linspace(0,30,31)
dist = binom.pmf(outcome_counts,30,0.39)

plt.bar(outcome_counts, dist)
plt.show()

#interpreting plot:
#If we repeatedly look at 30 days of bikesharing data, we'll find that 10 of the days had more than 5000 riders about 12.4% of the time. We'll find that 12 of the days had more than 5000 riders about 14.6% of the time.


#now with 10 days
outcome_counts = linspace(0,10,11)
dist = binom.pmf(outcome_counts,10,0.39)
plt.bar(outcome_counts, dist)
plt.show()

#now with 100 days
outcome_counts = linspace(0,100,101)
dist = binom.pmf(outcome_counts,100,0.39)
plt.bar(outcome_counts, dist)
plt.show()



#plotting a line chart show better how the distribution starts seeming more "normal" with more days
outcome_counts = linspace(0,10,11)
outcome_probs = binom.pmf(outcome_counts,10,0.39)
plt.plot(outcome_counts, outcome_probs)
plt.show()

outcome_counts = linspace(0,100,101)
outcome_probs = binom.pmf(outcome_counts,100,0.39)
plt.plot(outcome_counts, outcome_probs)
plt.show()




#cumulative density distribution
outcome_counts = linspace(0,30,31)
outcome_probs = binom.cdf(outcome_counts,30,0.39)
plt.plot(outcome_counts, outcome_probs)
plt.show()

