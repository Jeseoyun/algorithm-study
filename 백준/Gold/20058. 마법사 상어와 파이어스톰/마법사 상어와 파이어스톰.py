from collections import deque


def print_board(board):
    for lst in board:
        for elem in lst:
            print(elem, end=" ")
        print()


def select_tiles(N, l):
    crop_size = 2 ** l
    whole_size = 2 ** N
    selected = []

    for i in range(0, whole_size, crop_size):
        for j in range(0, whole_size, crop_size):
            selected.append((i, j))

    return selected


def spin_clockwise_90(A, l, x, y):
    crop_size = 2**l
    # 1. 원본 배열에서 바뀔 부분
    crop = [row[y:y+crop_size] for row in A[x:x+crop_size]]

    # 2. 회전 수행
    spin = list(zip(*crop[::-1]))

    # 3. 회전된 결과를 원본에 덮어쓰기
    for i in range(crop_size):
        for j in range(crop_size):
            A[x+i][y+j] = spin[i][j]


def count_near_ice(A, N, x, y):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    cnt = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= 2**N or ny < 0 or ny >= 2**N:
            continue

        if A[nx][ny] > 0:
            cnt += 1

    return cnt


def firestorm(A, N, l):
    # print(f"--- 파이어스톰 시작 (l={l}) ---")
    # print("원래 보드:")
    # print_board(A)

    # 1. 격자 나눈다
    selected = select_tiles(N, l)
    # print(f"선택된 부분 격자: {selected}")

    # 2. 부분 격자를 시계방향으로 90도 회전시킨다
    for x, y in selected:
        spin_clockwise_90(A, l, x, y)
    # print("회전 후 보드:")
    # print_board(A)
    # print()

    # 3. 주변에 얼음이 있는 칸이 2개 이하면 해당 칸의 얼음 양이 1 줄어든다
    ## 여기서 바로 얼음 감소를 적용하면 감소된 양이 다음 칸 계산에 반영되므로 감소할 칸을 찾아서 한 번에 반영해야 한다...
    decrease_ice = []
    for i in range(2**N):
        for j in range(2**N):
            if A[i][j] > 0 and count_near_ice(A, N, i, j) <= 2:
                decrease_ice.append((i, j))
    # print(f"감소할 얼음 칸: {decrease_ice}")

    for i, j in decrease_ice:
        A[i][j] -= 1

    # print("얼음 감소 후 보드:")
    # print_board(A)
    # print(f"--- 파이어스톰 종료 (l={l}) --- \n")


def get_max_connected_group_cnt(A, N):
    visited = [[0]*(2**N) for _ in range(2**N)]
    max_group_cnt = 0
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(2**N):
        for j in range(2**N):
            if A[i][j] <= 0:
                continue
            if visited[i][j]:
                continue

            queue = deque([(i, j)])
            visited[i][j] = 1
            cnt = 1

            while queue:
                x, y = queue.popleft()

                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy

                    if nx < 0 or nx >= 2**N or ny < 0 or ny >= 2**N:
                        continue

                    if visited[nx][ny]:
                        continue

                    if A[nx][ny] <= 0:
                        continue

                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1

            max_group_cnt = max(max_group_cnt, cnt)

    return max_group_cnt


def main():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2**N)]  # A: 칸에 있는 얼음 양, 격자 크기 (2**N)x(2**N)
    L = list(map(int, input().split()))  # 시전할 단계

    # 파이어스톰 스킬 시전
    for l in L:
        firestorm(A, N, l)

    # print("\n최종 보드 상태:")
    # print_board(A)

    total_ice = sum(map(sum, A))
    max_group_cnt = get_max_connected_group_cnt(A, N)

    print(total_ice)
    print(max_group_cnt)


if __name__ == "__main__":
    main()