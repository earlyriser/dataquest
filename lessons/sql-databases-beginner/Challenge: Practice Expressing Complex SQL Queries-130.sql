## 2. Use SELECT and LIMIT to Filter Results ##

SELECT College_jobs, Median, Unemployment_rate FROM recent_grads LIMIT 20

## 3. Use WHERE to Filter Results ##

SELECT Major FROM recent_grads WHERE Major_category='Arts' LIMIT 5

## 4. Express Criteria With Operators ##

SELECT Major, Total, Median, Unemployment_rate FROM recent_grads WHERE Major_category!='Engineering' AND (median <= 50000 OR Unemployment_rate > 0.065)

## 5. Order Your Results ##

SELECT Major FROM recent_grads WHERE Major_category!='Engineering' ORDER BY Major DESC LIMIT 20