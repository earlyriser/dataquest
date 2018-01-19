## 2. Calculating differences ##

female_diff = (10771 - 16280.5)/16280.5 
male_diff = (21790 - 16280.5)/16280.5 

## 3. Updating the formula ##

female_diff = ((10771 - 16280.5)**2)/16280.5 
male_diff = ((21790 - 16280.5)**2)/16280.5 

gender_chisq = female_diff +male_diff

## 4. Generating a distribution ##

import numpy as np
import matplotlib.pyplot as plt

chi_squared_values = []

for i in range(1000):
    series = np.random.random(32561,)
    series[series < .5] = 0
    series[series >= .5] = 1
            
    male_count = len(series[series == 0])
    female_count = len(series[series == 1])
    
    female_diff = ((female_count-16280.5)**2)/16280.5 
    male_diff = ((male_count-16280.5)**2)/16280.5 

    chi_squared = female_diff +male_diff
    chi_squared_values.append(chi_squared)
    
plt.hist(chi_squared_values)

## 6. Smaller samples ##

expected_f =162.805
expected_m =162.805
observed_f =107.71
observed_m =217.90

female_diff =  (observed_f-expected_f)**2/expected_m
male_diff =  (observed_m-expected_m)**2/expected_m

gender_chisq = female_diff + male_diff

## 7. Sampling distribution equality ##

import numpy as np
import matplotlib.pyplot as plt

chi_squared_values = []

for i in range(1000):
    sequence = np.random.random(300,)
    sequence[sequence<.5]=0
    sequence[sequence>=.5]=1
    
    male_count = len(sequence[sequence==0])
    female_count = len(sequence[sequence==1])
    
    male_diff = (male_count - 150)**2/150
    female_diff = (female_count - 150)**2/150
    
    chi_squared_values.append(male_diff+female_diff)
    
plt.hist(chi_squared_values)
    

## 9. Increasing degrees of freedom ##

wh_exp=26146.5
bl_exp=3939.9
ap_exp=944.3
ai_exp=260.5
ot_exp=1269.8

wh_obs=27816
bl_obs=3124
ap_obs=1039
ai_obs=311
ot_obs=271

def calculate(obs,exp):
    return (obs-exp)**2/exp

wh=calculate(wh_obs,wh_exp)
bl=calculate(bl_obs,bl_exp)
ap=calculate(ap_obs,ap_exp)
ai=calculate(ai_obs,ai_exp)
ot=calculate(ot_obs,ot_exp)

race_chisq = wh+bl+ap+ai+ot

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

observed =[27816,   3124,   1039,   311,    271]
expected =[26146.5, 3239.9, 944.3,  260.5,  269.8]

chisquare_value, race_pvalue = chisquare(observed, expected)