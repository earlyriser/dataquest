## 2. Calculating expected values ##

total_rows = 32561

males_over50k= total_rows * .241 * .669
males_under50k= total_rows * .759 * .669
females_over50k= total_rows * .241 * .331
females_under50k= total_rows * .759 * .331

## 3. Calculating chi-squared ##

from scipy.stats import chisquare

exp_m_over = 5249.8
exp_m_under = 16533.5
exp_f_over = 2597.4
exp_f_under = 8180.3

obs_m_over = 6662
obs_m_under = 15128
obs_f_over = 1179
obs_f_under = 9592


import numpy as np
observed =[obs_m_over, obs_m_under, obs_f_over, obs_f_under]
expected =[exp_m_over, exp_m_under, exp_f_over, exp_f_under]
chisq_gender_income, pvalue = chisquare(observed, expected)

## 4. Finding statistical significance ##

chisq_gender_income, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross tables ##

import pandas

table = pandas.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding expected values ##


from scipy.stats import chi2_contingency

crosstable = pandas.crosstab(income["sex"], [income["race"]])
print(table)

chisq_value, pvalue_gender_race, df, expected = chi2_contingency(crosstable)

pv_formatted = format(pvalue_gender_race, '.8f')