T = int(input()) # read a line with a single integer
for t in range(1, T + 1):
    s = input()
    i, j = map(int, input().split())
    n = len(s)
    x, y = (i - 1) % n, (j - 1) % n
    d1 = n - x
    d = (j - i + 1 - d1 - (y + 1)) // n
    f = s.count('B')
    if (j-i+1) <= n:
    	result = s[x:y+1].count('B')
    else:
    	result = f*d + s[x:n].count('B') + s[:y+1].count('B')
    print("Case #{}: {}".format(t, result))