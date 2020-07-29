# 4*2 [3*1]		3
# 4*3 [3*2]		10   
# 4*4 [3*3]		20		
# 4*5 [3*4]		30
# 5*5 [4*4]     50

T = int(input())
for t in range(1, T + 1):
	L, Righ = map(int, input().split())
	R, C = min(Righ, L) - 1, max(Righ, L) - 1
	b1 =  R * C # x < y
	if R == 1:
		result = b1
	else:
		b2 = (R-1)*(C-1)*2
		M = R + C + 1
		a = M - R * (R - 1)(2 * R + 3) * M // 6
		result = b1 + b2 + a
		result %= 10**9 + 7
	print("Case #{}: {}".format(t, result))