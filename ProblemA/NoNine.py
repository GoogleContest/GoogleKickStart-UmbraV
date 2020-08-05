T = int(input())
for t in range(1, T+1):
    F, R = map(int, input().split())
    lis = [x for x in range(F, R+1)]
    lis[:] = [x for x in lis if '9' not in str(x) and x % 9 != 0]
    result = len(lis)
    print("Case #{}: {}".format(t, result))
