T = int(input())
for t in range(1, T + 1):
    N = int(input())
    s = [int(x) for x in input().split()]
    h = [1]
    x = 1
    for i in range(1, N):
        lis = s[: i + 1]
        lis.sort(reverse=True)
        if lis[i] >= i:
            x += 1
        h.append(x)
    print("Case #{}: {}".format(t, h))
