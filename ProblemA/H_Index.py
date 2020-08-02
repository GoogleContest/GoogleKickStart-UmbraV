T = int(input())
for t in range(1, T + 1):
    N = int(input())
    s = [int(x) for x in input().split()]
    h = "1"
    x = 1
    for i in range(1, N):
        lis = s[: i + 1]
        lis.sort(reverse=True)
        # print("i = {} while Lis = {}".format(i, lis))
        if lis[x] > x:
            x += 1
            # print("lis[x] = {}, x = {}".format(lis[i], i))
        h += ' ' + str(x)
        # print("h = {}".format(h))
    print("Case #{}: {}".format(t, h))
