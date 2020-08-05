def f(p, cycle, paths):
    delete = []
    if not p:
        return paths
    else:
        set2 = set(cycle)
        for x in p:
            set1 = set(p[x])
            if set1.intersection(set2):
                paths[x - 1] += 1
                delete.append(x)
        for key in delete:
            del p[key]
        return f(p, cycle, paths)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    planets = {x: [] for x in range(1, N+1)}
    paths = [0] * N
    cycle = []
    result = 0
    for x in range(1, N + 1):
        L, R = map(int, input().split())
        if L in planets:
            planets[L].append(R)
        if R in planets:
            planets[R].append(L)
    for x in planets:
        if len(planets[x]) > 1:
            cycle.append(x)
    delete = [key for key in planets if key in cycle]
    for key in delete:
        del planets[key]
    result = f(planets, cycle, paths)
    print("Case #{}: {}".format(t, ' '.join(str(x) for x in result)))
