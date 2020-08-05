T = int(input())
for t in range(1, T + 1):
    N = int(input())
    a = [int(x) for x in input().split()]
    r = 0
    if N > 2:
        for i in range(1, N - 1):
            if a[i - 1] < a[i] and a[i] > a[i + 1]:
                r += 1
    print("Case #{}: {}".format(t, r))