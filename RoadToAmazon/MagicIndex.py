def magicIndex(arr):
  i, j  = 0, len(arr) - 1
  while i <= j:
    mid = i + (j - i ) // 2
    if arr[mid] > mid:
      j = mid - 1
    elif arr[mid] < mid:
      i = mid + 1
    else:
      return mid
  return -1

arr = [-1, 0, 1, 2, 4, 10]
print(magicIndex(arr))