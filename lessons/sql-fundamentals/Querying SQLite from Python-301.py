## 3. Connecting to the Database ##

import sqlite3

conn = sqlite3.connect("jobs.db")

## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])

query ="SELECT Major FROM recent_grads"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[0:2])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

q ="SELECT Major, Major_category FROM recent_grads"

five_results = cursor.execute(q).fetchmany(5)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

import sqlite3

conn = sqlite3.connect("jobs2.db")
cursor = conn.cursor()

q="SELECT Major FROM recent_grads ORDER BY Major DESC"

reverse_alphabetical=cursor.execute(q).fetchall()

conn.close()