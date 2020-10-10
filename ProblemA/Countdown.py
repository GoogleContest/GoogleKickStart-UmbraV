T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    a = [int(x) for x in input().split()]
    lis = [x for x in reversed(range(1, K + 1))]
    result = 0
    r = 0
    for i in range(N - K + 1):
        if a[i] == K:
            for x in range(K):
                if a[i + x] != lis[x]:
                    r = 0
                    break
                r += 1
        if r == K:
            result += 1
            r = 0

    """ Is it best to not use strings?
    if K == N:
        if a == lis:
            r = 1
        else:
            r = 0
    else:
        r = a.count(lis)
        """
    print("Case #{}: {}".format(t, result))