import fhm_unittest as unittest
import numpy as np
# Task 03: DUBER Fare Splitting
def findGroups(money, fare):
    neg=np.array([0]*len(money))
    c=0
    g=1
    ungrouped=np.array([0]*len(money))
    ugp=False
    cc=0
    g=1
    for i in range(len(money)):
        group=False
        if money[i]!=fare and i!=(len(money)-1):
            for j in range(i+1,len(money)):
                if j not in neg:
                    if (money[i]+money[j])==fare:
                        print(f"Group {g}: {money[i]}, {money[j]}")
                        g+=1
                        neg[c],neg[c+1]=i,j
                        c+=2
                        group=True
                        break
            if group==False and (i not in neg):
                ungrouped[cc]=money[i]
                cc+=1
                ugp=True
        elif money[i]==fare:
            print(f"group {g} : {money[i]}")
            g+=1
        elif i not in neg:
            ungrouped[cc]=money[i]
            cc+=1
            ugp=True
    if ugp==True:
        ungroup="Ungrouped : "
        for i in range(len(ungrouped)):
            if ungrouped[i]!=0:
                ungroup+=str(ungrouped[i])+" "
        print(ungroup)
        



print("///  Task 03: DUBER Fare Splitting  ///")
money = np.array( [120, 100, 150, 50, 30])
fare = 150
print(f'Task 3:')
findGroups(money, fare) # This should print

# Group 1 : 120, 30
# Group 2 : 100, 50
# Group 3 : 150


money = np.array( [60, 150, 60, 30, 120, 30])
fare = 180
print(f'Task 3:')
findGroups(money, fare) # This should print

# Group 1 : 60, 120
# Group 2 : 30, 150
# Ungrouped : 30 60