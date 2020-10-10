
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    lis = []
    for n in range(N):
        se = list(map(int, input().split()))
        lis += se
    lisa = sorted(lis)
    i, r = 0, 0
    while lisa:
        m = lisa[0] + K
        lisa = [elem for elem in lisa if elem >= m]
        if len(lisa) % 2 != 0:
            r -= 1
        r += 1
    print("Case #{}: {}".format(t, r))