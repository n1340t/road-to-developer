# shipments = [1, 2, 3]
# shipments = [4, 5,6, 7,2]
shipments = [18,14,12,10]


def shipmentImbalance(shipments):
    res = 0
    n = len(shipments)
    for k in range(1, n + 1):
        for x in range(n - k + 1):
            res += max(shipments[x:x+k]) - min(shipments[x:x+k])
            print(shipments[x:x+k])
    # for x in range(len(shipments) - 1):
    #     print(x+ 1, n - x - 1)
    #     res += (x + 1) * (shipments[x + 1] - shipments[x]) * (n - x - 1)

    return res


def shipmentImbalanceV2(shipments):
    N = len(shipments)
    ans = 0
    stack = []
    nextSmaller = [N] * N
    prevSmallerOrEqual = [-1] * N
    for i in range(N):
        n = shipments[i]
        while stack and n < shipments[stack[-1]]:
            nextSmaller[stack.pop()] = i
        stack.append(i)
    print(nextSmaller)
    stack = []
    for i in range(N-1, -1, -1):
        n = shipments[i]
        while stack and n <= shipments[stack[-1]]:
            prevSmallerOrEqual[stack.pop()] = i
        stack.append(i)
    print(prevSmallerOrEqual)
    for i in range(N):
        n = shipments[i]
        r = nextSmaller[i]
        l = prevSmallerOrEqual[i]
        print(l, r)
        ans += (i-l)*(r-i)*n  # [0]

    print(ans % (10**9 + 7))


# print(shipmentImbalance(shipments))
print(shipmentImbalanceV2(shipments))
