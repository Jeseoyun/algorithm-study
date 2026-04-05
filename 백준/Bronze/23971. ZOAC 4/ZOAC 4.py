def main():
    H, W, N, M = map(int, input().split())

    row_cnt = (H + N) // (N + 1)
    col_cnt = (W + M) // (M + 1)

    print(row_cnt * col_cnt)
    

if __name__ == "__main__":
    main()