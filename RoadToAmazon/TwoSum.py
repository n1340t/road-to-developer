'''
Problem statement:
You are given an array of n integers and a number k. Determine whether there is a pair
of elements in the array that sums to exactly k. For example, given the array [1, 3, 7] and
k = 8, the answer is “yes,” but given k = 6 the answer is “no.”
'''
# complexity is O(n^2)
def two_sum_v1(arr: list, target: int) -> bool:
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == target:
        return True
  return False
# time complexity is O(n) and space complexity is O(n)
def two_sum_v2(arr: list, target: int) -> bool:
  hash_map = {}
  for x in arr:
    if hash_map.get(target - x):
      return True
    hash_map[x] = 1
  return False
#
def two_sum_v3(arr: list, target: int) -> bool:
  lhs, rhs = 0, len(arr) - 1
  arr.sort()
  while (lhs < rhs):
    _sum = arr[lhs] + arr[rhs]
    if _sum == target:
      return True
    elif _sum < target:
      lhs += 1
    else:
      rhs -= 1
  return False

res1 = two_sum_v1([1,3,7], 8)
res2 = two_sum_v2([1,3,7], 8)
res3 = two_sum_v3([1,3,7], 8)

print(res1, res2, res3)