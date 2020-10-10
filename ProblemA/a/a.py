
T = int(input())

for t in range(1, T+1):
    N, X = map(int, input().split())
    lis = list(map(int, input().split()))
    dic = {k: 0 for (k, v) in enumerate(lis)}
    for i, m in enumerate(lis):
        if m <= X:
            dic[i] = 1

        else:
            a = m // X
            b = m % X
            if b == 0:
                dic[i] = a
            else:
                a += 1
                dic[i] = a
    r = list(sorted(dic.items(), key=lambda x:x[1]))
    s = ""
    
    for y in r:
        s += " " + str(y[0]+1)
    print("Case #{}:{}".format(t, s))