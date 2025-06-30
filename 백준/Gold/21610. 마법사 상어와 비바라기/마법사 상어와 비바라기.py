dxy = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def move_cloud(cloud, N, d, s):
    new_cloud = [[0]*N for _ in range(N)]
    cloud_pos = []

    for x in range(N):
        for y in range(N):
            if cloud[x][y] == 0:
                continue

            nx = (x + dxy[d-1][0] * s) % N
            ny = (y + dxy[d-1][1] * s) % N

            new_cloud[nx][ny] = 1
            cloud_pos.append((nx, ny))

    return new_cloud, cloud_pos


def water_copy_bug_magic(basket, N, bug_pos):
    for x, y in bug_pos:
        water_basket_cnt = 0

        # 1. 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 찾기
        for idx, (dx, dy) in enumerate(dxy):
            if idx%2 == 0:  # 대각선 방향 필터링
                continue

            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if basket[nx][ny] > 0:
                water_basket_cnt += 1

        # 2. 물 있는 바구니 수만큼 물의 양 증가
        basket[x][y] += water_basket_cnt


def generate_cloud(basket, N, prev_cloud_pos):
    new_cloud = [[0]*N for _ in range(N)]
    prev_cloud_pos = set(prev_cloud_pos)

    for i in range(N):
        for j in range(N):
            if basket[i][j] >= 2 and (i, j) not in prev_cloud_pos:
                new_cloud[i][j] = 1
                basket[i][j] -= 2

    return new_cloud


def main():
    N, M = map(int, input().split())
    basket = [list(map(int, input().split())) for _ in range(N)]

    # 비바라기 시전 시 초기 구름
    cloud = [[0]*N for _ in range(N)]
    for sx, sy in [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]:
        cloud[sx][sy] = 1

    # print_board(cloud)

    for _ in range(M):
        d, s = map(int, input().split())  # 방향, 이동 칸 수

        # 1. 모든 구름이 d방향 s만큼 이동
        cloud, cloud_pos = move_cloud(cloud, N, d, s)
        # print("구름")
        # print_board(cloud)

        # print("전")
        # print_board(basket)

        # 2. 구름이 있는 칸의 바구니에 저장된 물 +1
        # 3. 구름 모두 사라짐
        for x, y in cloud_pos:
            basket[x][y] += 1
            cloud[x][y] = 0

        # print("후")
        # print_board(basket)

        # 4. 물복사 버그 마법 시전
        water_copy_bug_magic(basket, N, cloud_pos)

        # 5. 구름 다시 만들기
        cloud = generate_cloud(basket, N, cloud_pos)

    # print_board(basket)
    print(sum(map(sum, basket)))


if __name__ == "__main__":
    main()