T = int(input())
for t in range(1, T + 1):
    N = int(input())
    s = [int(x) for x in input()]
    if N % 2 == 0:
        a = N // 2
    else:
        a = N // 2 + 1
    s1 = [sum(s[x: x + a]) for x in range(a+1)]
    s2 = [sum(s[x: x + a]) for x in range(a - 1, N + 1)]
    r = max(max(s1), max(s2))
    print("Case #{}: {}".format(t, r))
