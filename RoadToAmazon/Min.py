arr = [187, 885, 456, 357, 729, 56, 924, 144, 699, 478, 541, 126, 710, 707, 490, 671, 251, 105, 601, -880]

def minArr(arr: list):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    m1 = minArr(arr[0:mid])
    m2 = minArr(arr[mid:])
    return min(m1, m2)

res = minArr(arr)
print(res)