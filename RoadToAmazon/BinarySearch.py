#Note: right can be either last index or array length.
#Either options will have slightly different implementation
def binarySearch(list: list, key: int, left: int, right: int ):
  if right < left:
    return -1
  
  mid = left + (right - left) // 2
  if list[mid] > key:
    # since // 2 return nearest integer (like floor), we don't need to subtract mid 1
    return binarySearch(list, key, left, mid)
  elif list[mid] < key:
    # already check mid, exclude mid by add 1
    return binarySearch(list, key, mid + 1, right)
  return mid

def binarySearchV2(list, key, left, right):
  while(left <= right):
    mid = left + (right - left) // 2
    if list[mid] > key:
      right = mid
    elif list[mid] < key:
      left = mid + 1
    else: 
      return mid
  return -1

list = [1,2,3,4,5,6]
res = binarySearch(list, 6, 0, len(list) - 1)
print('Position', res)