t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    L, R = map(int, input().split()) # Need to know more about map
    val = min(L, R)
    result = val * (val + 1) // 2 # This is very basic math, you should've known
    print("Case #{}: {}".format(i, result))