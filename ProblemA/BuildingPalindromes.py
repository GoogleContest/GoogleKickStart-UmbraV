T = int(input())
for t in range(1, T + 1):
    n, q = map(int, input().split())
    s = input()
    result = q
    for i in range(q):
        x, y = map(int, input().split())
        s1 = [x for x in s[x - 1:y]]
        set1 = set(s1)
        odd = 0
        for x in set1:
            if s1.count(x) % 2 != 0:
                odd += 1
            if odd > 1:
                result -= 1
                break
    print("Case #{}: {}".format(t, result))
