T = int(input())
for t in range(1, T + 1):
    N = int(input())
    a = [int(x) for x in input().split()]
    r = 0
    m = 0
    if N == 1:
        r += 1
    else:
        for i in range(N - 1):
            if a[i] > m and a[i] > a[i + 1]:
                r += 1
                #print("r: {}".format(r))
            m = max(a[i], m)
            #print("m:{}".format(m))
        if a[N - 1] > m:
            r += 1
            #print("R2:{} m2: {}".format(r, m))
    print("Case #{}: {}".format(t, r))