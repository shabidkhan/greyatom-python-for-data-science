# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census = np.concatenate((data,np.array(new_record)),axis=0)

age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
# print(age_std)

race_0 = (census[0:0,2])
race_1 = (census[0:1,2])
race_2 = (census[0:2,2])
race_3 = (census[0:3,2])
race_4 = (census[0:4,2])
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

senior_citizens = census[:,0]>60
working_hours_sum = np.sum(census[senior_citizens,6])
avg_working_hours = np.mean(census[senior_citizens,6])
print(avg_working_hours)

high = census[:,1]>10
low = census[:,1]<=10

avg_pay_high = np.mean(census[high,7])
avg_pay_low = np.mean(census[low,7])

print(avg_pay_high,avg_pay_low)




