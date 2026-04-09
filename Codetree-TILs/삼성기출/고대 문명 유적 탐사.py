from collections import deque
import copy


SIZE = 5
dxy = [(-1, 0), (0, 1), (0, -1), (1, 0)]


def rotate_clockwise(grid, cx, cy, k):
    new_grid = copy.deepcopy(grid)

    for _ in range(k):
        temp = [row[cy-1:cy+2] for row in new_grid[cx-1:cx+2]]

        for i in range(3):
            for j in range(3):
                new_grid[cx-1+j][cy-1+(2-i)] = temp[i][j]

    return new_grid


def connected_pieces(grid):
    pos = set()
    visited = [[False] * SIZE for _ in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            if visited[i][j]:
                continue

            queue = deque([(i, j)])
            visited[i][j] = True
            component = [(i, j)]
            value = grid[i][j]

            while queue:
                x, y = queue.popleft()

                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy

                    if nx < 0 or nx >= SIZE or ny < 0 or ny >= SIZE:
                        continue
                    if visited[nx][ny]:
                        continue
                    if grid[nx][ny] != value:
                        continue

                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    component.append((nx, ny))

            if len(component) >= 3:
                pos.update(component)

    return pos


def main():
    K, M = map(int, input().split())
    pieces = [list(map(int, input().split())) for _ in range(SIZE)]
    numbers = deque(map(int, input().split()))

    # 턴마다 실행
    total_values = []
    for _ in range(K):
        # print(f"{_+1} 턴입니다.")
        # 1. 탐사 진행
        # 모든 중심좌표에 대해 회전 시도
        values = []  # (가치, 회전횟수, 중심좌표 열, 중심좌표 행)
        turn_value = 0
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    # 1) 회전
                    new_pieces = rotate_clockwise(pieces, i, j, k)

                    # 2) 1차 획득 가치 계산
                    # 숫자 같은거 개수 찾아저 점수 계산
                    connected = connected_pieces(new_pieces)
                    values.append((len(connected), k, j, i))

        # 2. 유물 획득
        # 최댓값 찾아서 없애고 값 채워넣기
        values.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
        val, k, y, x = values[0]

        if val == 0:
            continue

        pieces = rotate_clockwise(pieces, x, y, k)
        replace_pos = list(connected_pieces(pieces))

        # 3. 연쇄 획득
        while replace_pos:
            # print("바꿀좌표:", replace_pos)
            replace_pos.sort(key=lambda x: (x[1], -x[0]))  # (열 번호, 행 번호)
            turn_value += len(replace_pos)

            for x, y in replace_pos:
                pieces[x][y] = numbers.popleft()

            replace_pos = list(connected_pieces(pieces))

        if turn_value:
            # print(f"최종 값: {turn_value}")
            total_values.append(turn_value)

    print(*total_values, sep=" ")


if __name__ == "__main__":
    main()

