def main():
    N = int(input())
    
    # 3n + 5m = N 을 만족하는 (n, m) 중 n + m 이 최소인 것을 찾으면 된다
    max_m = N//5 + 1
    max_n = N//3 + 1
    
    min_comb = float('inf')
    
    for m in range(max_m):
        for n in range(max_n):
            if 5*m + 3*n == N:
                min_comb = min(min_comb, m + n)
            elif 5*m + 3*n > N:
                break
            
    if min_comb == float('inf'):
        min_comb = -1
            
    print(min_comb)


if __name__ == "__main__":
    main()