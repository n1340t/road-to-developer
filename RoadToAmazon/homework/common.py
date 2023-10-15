from collections import defaultdict
import bisect
import util as Util

util = Util.Utility()
def twoSum1(arr: list[int], k: int) -> bool:
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] + arr[j] == k:
        return True
  return False

def twoSum2(arr: list[int], k: int) -> bool:
    arr.sort()
    i, j = 0, len(arr) - 1
    while i < j:
      target = arr[i] + arr[j]
      if target == k:
        return True
      elif target > k:
        j -= 1
      else:
        i += 1
    return False

def twoSum3(arr: list[int], k: int) -> bool:
    hashMap = defaultdict(lambda: 0)
    for val, i in enumerate(arr):
      if hashMap[k - val]:
        return True
      hashMap[val] = 1
    return False

def twoSum4(arr: list[int], k: int) -> bool:
    arr.sort()
    for i in range(len(arr)):
      x = bisect.bisect_left(arr, k - arr[i], i + 1, len(arr))
      # bisect_left return leftmost index that when we insert at that index, the order is reserved
      # if target is greater than max element => index is arr length
      # if target is between two number => index is the position of greater element. For example [3,4], target = 3.5
      if x != len(arr) and arr[x] == k - arr[i]:
        return True
    return False

if __name__ == '__main__':
  print('-----Two Sum -----')
  arr = [1,2,3,4,5]
  print('Two sum version 1: ', twoSum1(arr, 5))
  print('Two sum version 2: ', twoSum2(arr, 5))
  print('Two sum version 3: ', twoSum3(arr, 5))
  print('Two sum version 4: ', twoSum4(arr, 5))