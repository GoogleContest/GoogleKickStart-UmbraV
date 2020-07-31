T = int(input())
for t in range(1, T + 1):
    N, P = map(int, input().split())
    lis = []
    s = 2 ** N
    for x in range(P):
        lis.append(input())  # list of forbidden strings
    lis.sort(key=len, reverse=True)
    forbidden = lis.copy()
    for i in range(P):
        for j in reversed(range(P)):
            if lis[j] in lis[i]:
                forbidden.remove(lis[j])
    for y in forbidden:
        s -= 2**(N-len(y))
    print("Case #{}: {}".format(t, s))

