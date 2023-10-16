from collections import defaultdict
import bisect
import util as Util

util = Util.Utility()

def twoSum1(arr: list[int], k: int) -> bool:
  N = len(arr)
  for i in range(N):
    for j in range(i + 1, N):
      if arr[i] + arr[j] == k:
        return True
  return False

def twoSum2(arr: list[int], k: int) -> bool:
  N = len(arr)
  hashMap = {}
  for i in range(N):
    if hashMap.get(k - arr[i], 0):
      return True
    hashMap[arr[i]] = 1
  return False

def twoSum3(arr: list[int], k: int) -> bool:
  N = len(arr)
  arr.sort()
  i, j = 0, N - 1
  while i < j:
    target = arr[i] + arr[j]
    if target > k:
      j -= 1
    elif target < k:
      i += 1
    else:
      return True
  return False

def twoSum4(arr: list[int], k: int) -> bool:
  arr.sort()
  N = len(arr)
  for i in range(N):
    x = bisect.bisect_left(arr, k - arr[i], i + 1, N)
    if x != N and arr[x] == k - arr[i]:
      return True
  return False

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