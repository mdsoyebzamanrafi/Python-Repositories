import fhm_unittest as unittest
import numpy as np
#Task 01: Merge Lineup
def mergeLineup(pokemon_1, pokemon_2):
  result = np.array([0]*len(pokemon_1))
  c=len(pokemon_1)-1
  for i in range(len(pokemon_1)):
    if pokemon_1[i]!=None and pokemon_2[c]!=None:
        result[i]=pokemon_1[i]+pokemon_2[c]
        c-=1
    elif pokemon_1[i]!=None and pokemon_2[c]==None:
        result[i]=pokemon_1[i]
        c-=1
    elif pokemon_1[i]==None and pokemon_2[c]!=None:
        result[i]=pokemon_2[c]
        c-=1
    else:
       result[i]=0
       c-=1
  return result

print("///  Task 01: Merge Lineup  ///")
pokemon_1 = np.array([12, 3, 25, 1, None])
pokemon_2 = np.array([5, -9, 3, None, None] )
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') # This should print [12, 3, 28, -8, 5]
unittest.output_test(returned_value, np.array([12, 3, 28, -8, 5]))
pokemon_1 = np.array([4, 5, -1, None, None])
pokemon_2 = np.array([2, 27, 7, 12, None])
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') # This should print [4,17,6,27,2]
unittest.output_test(returned_value, np.array([4,17,6,27,2]))