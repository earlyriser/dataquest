## 1. Introduction ##

import sqlite3

conn = sqlite3.connect("factbook.db")

facts = conn.execute("SELECT * from facts").fetchall()
facts_count = len(facts)
print(facts)

## 2. Counting the Number of Rows in SQL ##

conn = sqlite3.connect("factbook.db")

resp = conn.execute("SELECT COUNT(birth_rate) FROM facts").fetchall()

birth_rate_count = resp[0]

## 3. Finding a Column's Minimum and Maximum Values in SQL ##

conn = sqlite3.connect("factbook.db")

resp1 = conn.execute("SELECT MIN(population_growth) from facts").fetchall()
resp2 = conn.execute("SELECT MAX(death_rate) from facts").fetchall()

min_population_growth = resp1[0][0]
max_death_rate = resp2[0][0]

## 4. Calculating Sums and Averages in SQL ##

conn = sqlite3.connect("factbook.db")

resp1 = conn.execute("SELECT SUM(area_land) from facts").fetchall()
resp2 = conn.execute("SELECT AVG(area_water) from facts").fetchall()

total_land_area = resp1[0][0]
avg_water_area = resp2[0][0]

## 5. Combining Multiple Aggregation Functions ##

conn = sqlite3.connect("factbook.db")

q = "SELECT AVG(population), SUM(population), MAX(birth_rate) FROM facts;"

resp = conn.execute(q).fetchall()

mean_pop =resp[0][0]
sum_pop =resp[0][1]
max_birth_rate =resp[0][2]




## 6. Aggregating Values for a Subset of the Data ##

conn = sqlite3.connect("factbook.db")

q = "SELECT AVG(population_growth) FROm facts WHERE population > 10000000"


resp = conn.execute(q).fetchall()

population_growth =resp[0][0]

## 7. Selecting Unique Rows ##

conn = sqlite3.connect("factbook.db")

q = "SELECT DISTINCT birth_rate FROM facts"

unique_birth_rates = conn.execute(q).fetchall()

## 8. Aggregating Unique Values ##

conn = sqlite3.connect("factbook.db")
q1 = "SELECT AVG(DISTINCT birth_rate) FROM facts WHERE population > 20000000;"
q2 = "SELECT SUM(population) FROM facts WHERE area_land > 1000000;"

average_birth_rate = conn.execute(q1).fetchall()
sum_population = conn.execute(q2).fetchall()

## 9. Performing Arithmetic in SQL ##

conn = sqlite3.connect("factbook.db")

population_growth_millions = conn.execute("SELECT population_growth / 1000000.0 FROM facts;").fetchall()
print(population_growth_millions)

## 10. Performing Arithmetic Between Columns ##

conn = sqlite3.connect("factbook.db")
next_year_population = conn.execute("SELECT (1 + (population_growth/100)) * population FROM facts;").fetchall()
print(next_year_population)