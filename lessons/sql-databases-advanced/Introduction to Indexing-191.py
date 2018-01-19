## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")

query = "PRAGMA table_info(facts)"
schema = conn.execute(query).fetchall()

for row in schema:
    print(row)

## 3. Explain query plan ##

import sqlite3
conn = sqlite3.connect("factbook.db")

query = "EXPLAIN QUERY PLAN SELECT * FROM facts WHERE area>40000"
query_plan_one = conn.execute(query).fetchall()

query = "EXPLAIN QUERY PLAN SELECT area FROM facts WHERE area>40000"
query_plan_two = conn.execute(query).fetchall()

query = "EXPLAIN QUERY PLAN SELECT * FROM facts WHERE name='Czech Republic'"
query_plan_three = conn.execute(query).fetchall()

print(query_plan_one)
print(query_plan_two)
print(query_plan_three)

## 5. Time complexity ##

import sqlite3
conn = sqlite3.connect("factbook.db")

query = "EXPLAIN QUERY PLAN SELECT * FROM facts WHERE id=20"
query_plan_four = conn.execute(query).fetchall()

print(query_plan_four)

## 9. All together now ##

import sqlite3
conn = sqlite3.connect("factbook.db")

query = "EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population>10000"
query_plan_six = conn.execute(query).fetchall()

query="CREATE INDEX IF NOT EXISTS pop_idx ON facts(population)"
conn.execute(query)

query = "EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population>10000"
query_plan_seven = conn.execute(query).fetchall()

print(query_plan_six)
print(query_plan_seven)