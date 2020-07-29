# 4*2 [3*1]		3
# 4*3 [3*2]		10   
# 4*4 [3*3]		20		
# 4*5 [3*4]		30
# 5*5 [4*4]     50

T = int(input())
for t in range(1, T + 1):
    L, Righ = map(int, input().split())
    R, C = min(Righ, L), max(Righ, L)
    r = (R ** 4) / 12 - C * (R ** 3) / 6 - (R ** 2) / 2 + R - 1 / 2
    result = int(r) % ((10 ** 9) + 7)
    print("Case #{}: {}".format(t, result))