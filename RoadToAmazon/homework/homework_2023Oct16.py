from collections import defaultdict
import bisect
import util as Util

util = Util.Utility()

def twoSum1(arr: list[int], k: int) -> bool:
  N = len(arr)
  for i, val1 in enumerate(arr):
    for j, val2 in enumerate(arr[i+1:]):
      if val1 + val2 == k:
        return True
  return False

def twoSum2(arr: list[int], k: int) -> bool:
  N = len(arr)
  arr.sort()
  for i, val in enumerate(arr):
    x = bisect.bisect_left(arr, k - val, i + 1, N)
    if x != N and arr[x] == k - val:
      return True
  return False

def twoSum3(arr: list[int], k: int) -> bool:
  N = len(arr)
  arr.sort()
  i, j = 0 , N - 1
  while i < j:
    target = arr[i] + arr[j]
    if target > k:
      j -= 1
    elif target == k:
      return True
    else:
      i += 1
  return False

def twoSum4(arr: list[int], k: int) -> bool:
  N = len(arr)
  hashMap = {}
  for i, val in enumerate(arr):
    if hashMap.get(k - val, 0):
      return True
    hashMap[val] = 1
  return False

def binarySearch(arr: list[int], k: int):
  pass
  
if __name__ == '__main__':
  print('-----Two Sum -----')
  arr = [1,2,3,4,5]
  print('Two sum version 1: ', twoSum1(arr, 5))
  print('Two sum version 4: ', twoSum1(arr, 10))
  print('Two sum version 2: ', twoSum2(arr, 5))
  print('Two sum version 4: ', twoSum2(arr, 10))
  print('Two sum version 3: ', twoSum3(arr, 5))
  print('Two sum version 4: ', twoSum3(arr, 10))
  print('Two sum version 4: ', twoSum4(arr, 5))
  print('Two sum version 4: ', twoSum4(arr, 10))