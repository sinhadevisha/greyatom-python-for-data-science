# --------------
# Importing header files
import numpy as np
# Path of the file has been stored in variable called 'path'
#New record
new_record=np.array([[50,9,4,1,0,0,40,0]])
#Code starts here
data=np.genfromtxt(path,delimiter=",",skip_header=1)
print("Data:\n\n",data)
print("\nType of data:\n\n",type(data))
census=np.concatenate((data[:],new_record),axis=0)
print(census)


# --------------
#Code starts here
import numpy as np
age=np.array(census[0:,0])
print(age)
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)



# --------------
#Code starts here
import numpy as np
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
len_arr=[len_0,len_1,len_2,len_3,len_3,len_4]
minority_race=len_arr.index(min(len_arr))
print("Minority",minority_race)


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
working_hours_sum=np.sum(senior_citizens[:,6])
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print("Average Working Hours",avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
print("Average Higher Pay",avg_pay_high)
avg_pay_low=np.mean(low[:,7])
print("Average Lower Pay",avg_pay_low)
if avg_pay_high>avg_pay_low: print("True")
else: print("False")


