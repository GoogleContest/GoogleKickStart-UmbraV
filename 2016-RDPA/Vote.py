t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n, m = map(int, input().split()) # Need to know more about map
    result = (n-m)/(n+m)
    print("Case #{}: {:.8f}".format(i, result))