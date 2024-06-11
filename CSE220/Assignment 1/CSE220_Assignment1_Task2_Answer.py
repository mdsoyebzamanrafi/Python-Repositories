import fhm_unittest as unittest
import numpy as np
# Task 02: Discard Cards

def discardCards(cards, t):
  idx_track=np.zeros(len(cards))
  c=0
  for i in range(len(cards)):
    if cards[i]==t:
      idx_track[c]=i
      c+=1
  print(idx_track)
  arr=np.array([0]*len(cards))
  idx=0
  for i in range(len(cards)):
    if i==idx_track[0] or i==idx_track[2]:
      continue
    else:
      arr[idx]=int(cards[i])
      idx+=1
  print(arr)
  return arr



print("///  Task 02: Discard Cards  ///")
cards = np.array([1,3,7,2,5,2,2,2,0])
returned_value = discardCards(cards, 2)
print(f'Task 2: {returned_value}') # This should print [1,3,7,5,2,2,0,0,0]
unittest.output_test(returned_value, np.array([1,3,7,5,2,2,0,0,0]))

cards = np.array([5,5,5,0,0])
returned_value = discardCards(cards, 5)
print(f'Task 2: {returned_value}') # This should print [5,0,0,0,0]
unittest.output_test(returned_value, np.array([5,0,0,0,0]))