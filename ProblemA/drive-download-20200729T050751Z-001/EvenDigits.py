T = int(input())
for t in range(1, T+1):
	str = input()
	number = int(str)
	lis = [int(x) for x in str] #list
	n = len(lis)
	result = 0
	r, rbig, rmsall = [], [], []
	for i, v in enumerate(lis):
		if v == 9 and i != 0:
			r = lis[:i]+[8]*(n-i)
			r1 = sum(d * 10**i for i, d in enumerate(r[::-1]))
			result = abs(r1-number)
			break
		elif v == 9 and i == 0:
			r = [8]*n
			r1 = sum(d * 10**i for i, d in enumerate(r[::-1]))
			result = abs(r1-number)
			break
		elif v % 2 != 0:
			rbig = lis[:i] + [v+1] + [0]*(n-i-1)
			rsmall = lis[:i] + [v-1] + [8] *(n-i-1)
			r2 = sum(d * 10**i for i, d in enumerate(rbig[::-1]))
			result1 = abs(r2-number)
			r3 = sum(d * 10**i for i, d in enumerate(rsmall[::-1]))
			result2 = abs(r3-number)
			result = min(result1, result2)
			break
		"""
	if r is not None:
		r1 = "".join(str(digit) for digit in r)
		print(r1)
		"""
		"""
	elif rbig or rsmall:
		result = min(abs(magic(rbig)-number), abs(magic(rsmall)-number))
		"""
	print("Case #{}: {}".format(t, result))