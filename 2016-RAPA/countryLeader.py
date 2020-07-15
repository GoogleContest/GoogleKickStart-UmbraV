# My first accepted answers! :D
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
	n = int(input()) # How many names there are in this test case
	names = {}
	for x in range(n):
		string = input()
		name = set()
		for s in string:
			if s.isupper() and s.isalpha():
				name.add(s)
		m = len(name)
		if m not in names:
			names[m] = []
		names[m].append(string)
	maxV = max(names)
	r = sorted(names[maxV])
	result = r[0]
	print("Case #{}: {}".format(i, result))

# check out .format's specification for more formatting options

# use set to get the largest number
# maybe a hashtable, with their names into sets
# get max of a list, or xor operation
"""
name = ""
for char in string:
	if char.isalpha():
		name += char
namelist = name.split('') 
# get the xor result and input it as dictionaty key
# get the largest key
# find the leader
"""