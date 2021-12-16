def sellProfit(arr: list):
    if len(arr) <= 1:
        return 0

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    leftBest = sellProfit(left)
    rightBest = sellProfit(right)
    crossBest = max(right) - min(left)

    return max(leftBest, rightBest, crossBest)


listA = [93, 52, 56, 145, 188, 192, 9, 16]
res = sellProfit(listA)
print('max profit', res)
