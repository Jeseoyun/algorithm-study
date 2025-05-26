def main():
    n = int(input())
    triangle = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        if i==0:
            continue
        for j in range(i+1):
            if j==0:
                triangle[i][j] += triangle[i-1][j]
            elif j==i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])


    print(max(triangle[-1]))


if __name__ == "__main__":
    main()