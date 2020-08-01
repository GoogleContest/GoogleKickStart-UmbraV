T = int(input())
for t in range(1, T + 1):
    N, P = map(int, input().split())
    lis = []
    s = 2 ** N
    for x in range(P):
        lis.append(input())  # list of forbidden strings
    lis.sort(key=len, reverse=True)
    forbidden = lis.copy()
    for n, f in enumerate(forbidden):
        for i in range(n):
            if forbidden[i].startswith(f):
                if forbidden[i] in lis:
                    lis.remove(forbidden[i])
    for y in lis:
        s -= 2**(N-len(y))
    print("Case #{}: {}".format(t, s))

