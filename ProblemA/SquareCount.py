T = int(input())
for t in range(1, T + 1):
	L, Righ = map(int, input().split())
	R, C = min(Righ, L), max(Righ, L)
	a = 0
	for i in range(1, R):
		a += (R - i)*(C - i)* i
	a %= 10**9 + 7
	print("Case #{}: {}".format(t, a))