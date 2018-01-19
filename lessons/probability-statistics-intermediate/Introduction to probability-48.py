## 1. Probability basics ##

# Print the first two rows of the data.
flags.head()

bars_sorted = flags.sort_values(by="bars", ascending=[False])
most_bars_country = bars_sorted['name'].iloc[0]

pop_sorted = flags.sort_values(by="population", ascending=[False])
highest_population_country = pop_sorted['name'].iloc[0]

print(pop_sorted)

## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_probability = len([ elem for elem in flags['orange'] if elem == 1])/total_countries

stripe_probability = len([ elem for elem in flags['stripes'] if elem > 1])/total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = .5 ** 10

hundred_heads = .5 ** 100

test = (1/6)**2

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
total_countries = flags.shape[0]
total_red = len([ elem for elem in flags['red'] if elem == 1])

first_probability = (total_red)/total_countries
second_probability = (total_red-1)/(total_countries-1)
third_probability = (total_red-2)/(total_countries-2)

three_red= first_probability * second_probability * third_probability

## 5. Disjunctive probability ##

import math

start = 1
end = 18000

by_100 = end/100
hundred_prob = by_100/end

by_70 = math.floor(end/70)
seventy_prob = by_70/18000

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None

total = flags.shape[0]
red = flags[flags["red"] == 1].shape[0]/total
orange = flags[flags["orange"] == 1].shape[0]/total
red_orange =flags[(flags["red"] == 1) & (flags["orange"] == 1)].shape[0]/total


stripes = flags[flags["stripes"] == 1].shape[0]
bars = flags[flags["bars"] == 1].shape[0]

red_or_orange=red+orange-red_orange



stripes = flags[flags["stripes"] > 0].shape[0] / flags.shape[0]
bars = flags[flags["bars"] > 0].shape[0] / flags.shape[0]
stripes_and_bars = flags[(flags["stripes"] > 0) & (flags["bars"] > 0)].shape[0] / flags.shape[0]

stripes_or_bars = stripes + bars - stripes_and_bars

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = False

all_3_tails = (1/2)**3

heads_or = 1- all_3_tails