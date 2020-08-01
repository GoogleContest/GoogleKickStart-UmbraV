import itertools
T = int(input())
for t in range(1, T + 1):
    N, P = map(int, input().split())
    s = [int(x) for x in input().split()]
    s.sort(reverse=True)
    result = float('inf')
    s2 = [0] * (N - P + 1)
    for i in range(N - P + 1):
        for j in range(P):
            s2[i] += s[i + P]
    for i in range(N - P + 1):
        r = 0
        r = P*s[i] - s2[i]
        if r < result:
            result = r
    print("Case #{}: {}".format(t, result))
