## counting inversion
def mergeSortInversion(listA, temp, lo, hi):
  inv_count = 0
  if (hi - lo <= 1): return inv_count # base case
  mid = lo + (hi - lo) // 2
  # mergeSortInversion returns inv_count so we need to add inv_count here too
  inv_count += mergeSortInversion(listA, temp, lo, mid)
  inv_count += mergeSortInversion(listA, temp, mid, hi)
  
  inv_count += merge(listA, temp, mid, lo, hi)
  return inv_count

def merge(listA, temp, mid, lo, hi):
  i = lo
  j = mid
  inversion = 0
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
      inversion += mid - i
      j += 1
    elif listA[j] > listA[i]:
      temp[k] = listA[i]
      i += 1

  for k in range(lo, hi):
    listA[k] = temp[k]

  return inversion

listA = [93, 52, 56, 145, 188, 192, 9, 16]
temp = [None] * len(listA)
res = mergeSortInversion(listA, temp, 0 , len(listA))
print(res)