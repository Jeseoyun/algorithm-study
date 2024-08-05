def get_min_comb(N, max_m, max_n):
    min_comb = float('inf')
    
    for m in range(max_m): # 큰 숫자를 먼저 박기
        for n in range(max_n):
            if 5*m + 3*n == N:
                min_comb = min(min_comb, m + n)
            elif 5*m + 3*n > N:
                break
            
    return min_comb if min_comb != float('inf') else -1


# fail: 메모리 초과
def get_min_comb_dfs(N, m, n, comb):
    if 5*m + 3*n == N:
        comb.append(m + n)
        return 
    if 5*m + 3*n > N:
        return
    
    get_min_comb_dfs(N, m+1, n, comb)
    get_min_comb_dfs(N, m, n+1, comb)


def main():
    N = int(input())
    
    # 3n + 5m = N 을 만족하는 (n, m) 중 n + m 이 최소인 것을 찾으면 된다
    max_m = N//5 + 1
    max_n = N//3 + 1
    
    result = get_min_comb(N, max_m, max_n)
    # comb = []
    # get_min_comb_dfs(N, 0, 0, comb)
    # result = min(comb) if comb else -1
    
    print(result)


if __name__ == "__main__":
    main()
