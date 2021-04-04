def mergeSort(listA, temp, lo, hi):
  if (hi - lo <= 1): return # base case
  mid = lo + (hi - lo) // 2
  mergeSort(listA, temp, lo, mid)
  mergeSort(listA, temp, mid, hi)

  merge(listA, temp, mid, lo, hi)

def merge(listA, temp, mid, lo, hi):
  print(mid, lo, hi)
  i = lo
  j = mid
  for k in range(lo, hi):
    # Copy the rest of [lo, mid]
    # Put the logic j == hi first here to for edge case:
    # merge most left [10, 20] with [2, 3]
    if j == hi:
      temp[k] = listA[i]
      i += 1
    # copy the rest of [mid, hi]
    elif i == mid:
      temp[k] = listA[j]
      j += 1
    elif listA[j] < listA[i]:
      temp[k] = listA[j]
      j += 1
    elif listA[j] > listA[i]:
      temp[k] = listA[i]
      i += 1
  
  for k in range(lo, hi):
    listA[k] = temp[k]

listA = [93, 52, 56, 145, 188, 192, 9, 16]
temp = [None] * len(listA)
mergeSort(listA, temp, 0 , len(listA))
# print(len(listA))

for x in range(6,8):
  print(x)