from collections import deque


dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우/하/좌/상
dxy_8 = dxy + [(1, 1), (-1, 1), (1, -1), (-1, -1)]


def print_board(board):
    for arr in board:
        for elem in arr:
            print(elem, end=" ")
        print()


def sort_portop(grid, attack, N, M):
    # 우선순위대로 데이터 뽑아내기
    # 공격력, 공격횟수, 행+열, 열
    portop_info = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] <= 0:
                continue
            portop_info.append([grid[i][j], attack[i][j], i+j, j])

    sorted_portop = sorted(portop_info, key=lambda x: (x[0], -x[1], -x[2], -x[3]))
    return sorted_portop


def lazer_attack_path(grid, N, M, sx, sy, ex, ey):
    # 경로 상의 레이저 포탑들도 공격력의 절반만큼 공격을 받음
    queue = deque([(sx, sy, {(sx, sy)})])  # x, y, hist
    visited = [[False]*M for _ in range(N)]

    while queue:
        x, y, hist = queue.popleft()

        for dx, dy in dxy:
            nx, ny = (x + dx)%N, (y + dy)%M

            if grid[nx][ny] <= 0:  # 부서진 포탑 지날 수 없음
                continue

            if visited[nx][ny]:  # 이미 지나온 경로
                continue

            if (nx, ny) == (ex, ey):
                return hist

            queue.append((nx, ny, hist|{(nx, ny)}))
            visited[nx][ny] = True

    return []


def portan_attack_area(grid, N, M, sx, sy, ex, ey):
    area = {(sx, sy)}
    for dx, dy in dxy_8:
        nx, ny = (ex+dx)%N, (ey+dy)%M

        if (nx, ny) == (sx, sy):
            continue
        if (nx, ny) == (ex, ey):
            continue
        if grid[nx][ny] <= 0:
            continue

        area.add((nx, ny))

    return area


def powerful_portop(grid, N, M):
    powerful = 0
    for i in range(N):
        for j in range(M):
            powerful = max(powerful, grid[i][j])

    return powerful
  

def main():
    N, M, K = map(int, input().split())  # NxM, K번 턴
    grid = [list(map(int, input().split())) for _ in range(N)]
    attack_turn = [[0]*M for _ in range(N)]  # 몇 번 턴에 공격했는지

    for turn in range(1, K+1):
        # 1. 공격자, 타겟 선정
        sorted_portop = sort_portop(grid, attack_turn, N, M)

        if len(sorted_portop) == 1:
            break

        # print("포탑 정렬:", sorted_portop)
        attacker = sorted_portop[0]  # 공격력, 최근공격, 행+열, 열
        target = sorted_portop[-1]
        # print("공격자:", attacker)
        # print("타겟:", target)

        # 공격자
        ai, aj = attacker[2]-attacker[3], attacker[3]
        attack_turn[ai][aj] = turn
        grid[ai][aj] = attacker[0] + N + M  # 파워 증가
        attack_power = grid[ai][aj]

        # 타겟
        ti, tj = target[2]-target[3], target[3]

        # print("공격 전")
        # print_board(grid)

        # 2. 공격 대상 찾기
        # 1) 레이저 공격: 공격 대상 포탑까지 최단경로
        attack_path = lazer_attack_path(grid, N, M, ai, aj, ti, tj)

        # 2) 포탄 공격: 레이저 공격으로 경로 도달할 수 없으면
        if not attack_path:
            # print("포탑공격이당")
            attack_path = portan_attack_area(grid, N, M, ai, aj, ti, tj)

        # 공격 경로 및 타겟 모두 공격
        for (i, j) in attack_path:
            if (i, j) == (ai, aj):
                continue
            if (i, j) == (ti, tj):
                continue
            grid[i][j] -= (attack_power//2)

        # 타겟도 공격
        grid[ti][tj] -= attack_power

        # 4. 포탑 정비
        for i in range(N):
            for j in range(M):
                if grid[i][j] <= 0:
                    grid[i][j] = 0
                    continue

                if (i, j) in attack_path:
                    continue
                if (i, j) == (ai, aj):
                    continue
                if (i, j) == (ti, tj):
                    continue

                grid[i][j] += 1

    #     print("공격 후")
    #     print_board(grid)
    #
    # print("최종")
    print(powerful_portop(grid, N, M))


if __name__ == "__main__":
    main()
