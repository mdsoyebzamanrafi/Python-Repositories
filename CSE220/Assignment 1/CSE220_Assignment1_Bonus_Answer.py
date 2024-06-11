import fhm_unittest as unittest
import numpy as np
x=np.array([10,8,13,9,14,25,-5,20,7,7,4])
sum=0
count=0
stsum=0
for i in range(len(x)):
    sum+=x[i]
    count+=1
mean=sum/count
for i in range(len(x)):
    stsum+=(x[i]-mean)**2
var=stsum/count
stdev=var**0.5
print(mean)
print(stdev)