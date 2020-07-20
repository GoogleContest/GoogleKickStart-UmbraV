# 4*2 [3*1]		3
# 4*3 [3*2]		10   
# 4*4 [3*3]		20		
# 4*5 [3*4]		30
# 5*5 [4*4]     50
def helper(x, y):
	if x <= 1:
		return x*y
	else:
		return helper(x - 1, y - 1)
		
T = int(input())
for t in range(1, T + 1):
	L, Righ = map(int, input().split())
	R, C = min(Righ, L) - 1, max(Righ, L) - 1
	base =  R * C # x < y
