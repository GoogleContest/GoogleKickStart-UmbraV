T = int(input())
for t in range(1, T+1):
    N, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    a.sort()
    c = 1
    r = 0
    while a:
        i = 0
        a = [x for x in a if x >= c]
        n = len(a)
        if n >= k:
            r += k
            del a[:k]
            c += 1
        else:
            """
            print("a3:{}".format(a))
            print("n:{}".format(n))
            r += (k-n)
            print("r2:{}".format(r))
            a.clear()
            print("a4:{}".format(a))
            """
            if a:
                r += (k - n)
            a.clear()
    print("Case #{}: {}".format(t, r))
        