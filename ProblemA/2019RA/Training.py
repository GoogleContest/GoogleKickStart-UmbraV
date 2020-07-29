T = int(input()) # read a line with a single integer
for t in range(1, T + 1):
    n, p = map(int, input().split())
    lis = list(map(int, input().split()))
    lis.sort()
    result = 0
    f = max(lis, key=lis.count)
    index = lis.index(f)
    recurrence = lis.count(f)
    extra = p - recurrence
    r = []
    print(extra)
    for i in range(extra):
        sub = lis[index - i : index-i+p-1]
        a = sub[-1]
        b = 0
        print(sub)
        """
        for x in sub:
            if x < a:
                b += (a - x)
        r.append(b)
    result = min(r)
"""
    """
    max_left = left[-1]
    max_right = right[-1]
    for x in left:
        if x < max_left:
            l += max_left - x
    for y in right:
        if y < max_right:
            r += max_right - y
    result = min(x, y)
    """
    print("Case #{}: {}".format(t, result))