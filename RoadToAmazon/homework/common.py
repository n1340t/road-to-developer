def twoSum1(arr: List[int], k: int): boolean
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == k:
          return True
  return False