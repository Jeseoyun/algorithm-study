def diamond_area(k):
    area = []

    for i in range(-k, k + 1):
        for j in range(-k, k + 1):
            if abs(i) + abs(j) <= k:
                area.append((i, j))

    return area, k**2+(k+1)**2  # 좌표, 면적


def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    k = 0
    max_gold = 0

    while k <= 2*N :
        area, cost = diamond_area(k)

        for x in range(N):
            for y in range(N):
                gold_cnt = 0
                for dx, dy in area:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue

                    if grid[nx][ny]:
                        gold_cnt += 1

                if gold_cnt * M < cost:  # 손해본 경우
                    continue

                max_gold = max(max_gold, gold_cnt)

        k += 1

    print(max_gold)


if __name__ == "__main__":
    main()
    # print(diamond_area(0))