def dp(i, j, x, R, C, r, grid):
    if j == C:
        return r
    else:
        if grid[i][j] == 0 and grid[i + 1][j] == 0 and grid[i][j + 1] == 0 and grid[i + 1][j + 1] == 0:
            x += 1
            i += 1
            j += 1
            print("i1:{}, j1:{}".format(i, j))
            if i == R:
                return dp(0, j + 1, x, R, C, r, grid)
            return dp(i, j, x, R, C, r, grid)
        else:
            if x != 1:
                r.append(x)
            x = 1
            if i < R:
                return dp(i + 1, 0, x, R, C, r, grid)
            else:
                return dp(0, j+1, x, R, C, r, grid)


T = int(input())
for t in range(1, T + 1):
    R, C, K = map(int, input().split())
    grid = [[0 for j in range(C)] for i in range(R)]
    for k in range(K):
        l, r = map(int, input().split())
        grid[l][r] = 1
    x = 1
    r = []
    r = dp(0, 0, x, R-1, C-1, r, grid)
    print("Case #{}: {}".format(t, r))
