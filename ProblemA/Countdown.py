T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    a = input()
    print(a)
    lis = [str(x) for x in reversed(range(1, K + 1))]
    lis = " ".join(lis)
    print(lis)
    r = a.count(lis)
    print(r)
    print("Case #{}: {}".format(t, r))