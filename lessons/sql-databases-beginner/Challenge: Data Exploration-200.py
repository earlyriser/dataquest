## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")

q ="SELECT AVG(population) as pop_avg, AVG(population_growth) as pop_growth_avg,  AVG(birth_rate) as birth_rate_avg, AVG(death_rate) as death_rate_avg FROM facts"

r = conn.execute(q).fetchall()

pop_avg = r[0][0]
pop_growth_avg= r[0][1]
birth_rate_avg= r[0][2]
death_rate_avg= r[0][3]

## 2. Find Ranges ##

conn = sqlite3.connect("factbook.db")

averages = "select avg(population), MIN(population), MAX(population),avg(population_growth), MIN(population_growth), MAX(population_growth),avg(birth_rate), MIN(birth_rate), MAX(birth_rate), avg(death_rate), MIN(death_rate), MAX(death_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_min = avg_results[0][1]
pop_max = avg_results[0][2]

pop_growth_avg = avg_results[0][3]
pop_growth_min = avg_results[0][4]
pop_growth_max = avg_results[0][5]

birth_rate_avg = avg_results[0][6]
birth_rate_min = avg_results[0][7]
birth_rate_max = avg_results[0][8]

death_rate_avg = avg_results[0][9]
death_rate_min = avg_results[0][10]
death_rate_max = avg_results[0][11]


## 3. Filter Values ##

conn = sqlite3.connect("factbook.db")

averages = "select avg(population), MIN(population), MAX(population),avg(population_growth), MIN(population_growth), MAX(population_growth),avg(birth_rate), MIN(birth_rate), MAX(birth_rate), avg(death_rate), MIN(death_rate), MAX(death_rate) from facts  WHERE population < 2000000000 AND population > 0;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_min = avg_results[0][1]
pop_max = avg_results[0][2]

pop_growth_avg = avg_results[0][3]
pop_growth_min = avg_results[0][4]
pop_growth_max = avg_results[0][5]

birth_rate_avg = avg_results[0][6]
birth_rate_min = avg_results[0][7]
birth_rate_max = avg_results[0][8]

death_rate_avg = avg_results[0][9]
death_rate_min = avg_results[0][10]
death_rate_max = avg_results[0][11]


## 4. Predict Future Population Growth ##

import sqlite3
conn = sqlite3.connect("factbook.db")

q= '''
SELECT round(population + population * (population_growth/100), 0) FROM facts WHERE population < 7000000000 AND population > 0
and population is not null and population_growth is not null;
'''
projected_population= conn.execute(q).fetchall()


## 5. Explore Projected Population ##

import sqlite3
conn = sqlite3.connect("factbook.db")

proj_pop_query = '''
select round(min(population + population * (population_growth/100)), 0), 
round(max(population + population * (population_growth/100)), 0), 
round(avg(population + population * (population_growth/100)), 0)
from facts 
where population > 0 and population < 7000000000 and 
population is not null and population_growth is not null;
'''

proj_results = conn.execute(proj_pop_query).fetchall()

pop_proj_min = proj_results[0][0]
pop_proj_max = proj_results[0][1]
pop_proj_avg = proj_results[0][2]

print("Projected Population,", "Minimum: ", pop_proj_min)
print("Projected Population,", "Maximum: ", pop_proj_max)
print("Projected Population,", "Average: ", pop_proj_avg)