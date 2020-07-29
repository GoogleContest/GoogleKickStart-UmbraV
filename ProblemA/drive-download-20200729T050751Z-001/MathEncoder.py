import itertools

T = int(input())
for t in range(1, T + 1):
	n = int(input())
	lis = list(map(int, input().split()))
	s = list(itertools.combinations(lis, 2))
	r = 0
	for x in s:
		i = lis.index(x[0])
		j = lis.index(x[1])
		d = x[1] - x[0]
		r += d*pow(2,j-i-1)
	result = r % (10**9+7)
	print("Case #{}: {}".format(t, result))