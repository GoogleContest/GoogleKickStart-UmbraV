import itertools

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    s = list(map(int, input().split()))
    r = 0
    for i in range(2, n + 1):
        subs = list(itertools.combinations(s, i))
        for x in subs:
            r += x[-1] - x[0]
    result = r % (10**9+7)
    print("Case #{}: {}".format(t, result))