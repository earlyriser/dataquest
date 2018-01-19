## 2. Register the DataFrame as a Table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")

df.registerTempTable("census2010")

tables = sqlCtx.tableNames()

print(tables)

## 3. Querying ##

q = "SELECT age FROM census2010"
result = sqlCtx.sql(q)
result.show()

## 4. Filtering ##

q = "SELECT males, females FROM census2010 WHERE age > 5 AND age < 15"
sqlCtx.sql(q).show()

## 5. Mixing Functionality ##

q = "SELECT males, females FROM census2010"
sqlCtx.sql(q).describe().show()

## 6. Multiple tables ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')

df_2000 = sqlCtx.read.json("census_2000.json")
df_1990 = sqlCtx.read.json("census_1990.json")
df_1980 = sqlCtx.read.json("census_1980.json")

df_2000.registerTempTable('census2000')
df_1990.registerTempTable('census1990')
df_1980.registerTempTable('census1980')
tables = sqlCtx.tableNames()
print(tables)

## 7. Joins ##

q = """
 select census2010.total, census2000.total
 from census2010
 inner join census2000
 on census2010.age=census2000.age
"""
sqlCtx.sql(q).show()

## 8. SQL Functions ##

query = """
 select sum(census2010.total), sum(census2000.total), sum(census1990.total)
 from census2010
 inner join census2000
 on census2010.age=census2000.age
 inner join census1990
 on census2010.age=census1990.age
"""
sqlCtx.sql(query).show()