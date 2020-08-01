T = int(input())
for t in range(1, T + 1):
    N, M, Q = map(int, input().split())
    mlis = [int(x) for x in input().split()]
    qlis = [int(x) for x in input().split()]
    r = [0]*Q
    for i in range(M):
        for j in range(Q):
            if mlis[i] % qlis[j] == 0:
                r[j] -= 1
    for i, val in enumerate(qlis):
        r[i] += N // val
    result = sum(r)
    print("Case #{}: {}".format(t, result))
