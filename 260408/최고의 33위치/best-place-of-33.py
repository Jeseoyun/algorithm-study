dxy = [
    (-1, 0), (0, 1), (1, 0), (0, -1), 
    (-1, 1), (1, 1), (1, -1), (-1, -1)
    ]  # 3x3 격자 탐색


def get_coin(grid, sx, sy):
    coin = grid[sx][sy]

    for dx, dy in dxy:
        nx, ny = sx + dx, sy + dy

        coin += grid[nx][ny]
    
    return coin



def main():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_coin = 0
    for i in range(1, N-1):
        for j in range(1, N-1):  # 가운데 점 후보
            max_coin = max(max_coin, get_coin(grid, i, j))
    
    print(max_coin)


if __name__ == "__main__":
    main()