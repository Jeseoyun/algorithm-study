def solution(m, n, puddles):
    puddles = set(tuple(p) for p in puddles)
    
    if (1, 1) in puddles or (m, n) in puddles:
        return 0
    
    path = [[0]*m for _ in range(n)]
    path[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if (j+1, i+1) in puddles:  # 좌표 대칭시켜줘야 함...
                path[i][j] = 0
            else:
                if i > 0:
                    path[i][j] += path[i-1][j]
                if j > 0:
                    path[i][j] += path[i][j-1]
                
    return path[n-1][m-1] % 1000000007