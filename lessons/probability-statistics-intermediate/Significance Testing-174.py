## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

plt.hist(mean_group_a)
plt.show()
plt.hist(mean_group_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a

print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)

mean_differences=[]

for i in range(1000):
    group_a =[]
    group_b =[]
    for value in all_values:
        random = np.random.rand()
        if random > 0.5:
            group_a.append(value)
        else:
            group_b.append(value)
    mean_a = np.mean(group_a)
    mean_b = np.mean(group_b)
    iteration_mean_difference = mean_b - mean_a
    mean_differences.append(iteration_mean_difference)
    
plt.hist(mean_differences)

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}

for diff in mean_differences:
    val = sampling_distribution.get(diff, False)
    if val:
        sampling_distribution[diff] = val + 1
    else:
        sampling_distribution[diff] = 1
        
print( sampling_distribution)

## 8. P value ##

frequencies = []
mean_difference = 2.52
for i in sampling_distribution.keys():
    print(i)
    if i >= mean_difference:
        frequencies.append(sampling_distribution[i])
    
p_value = np.sum(frequencies)/1000
    