from collections import defaultdict, deque


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def print_board(grid):
    for arr in grid:
        for elem in arr:
            print(elem, end=" ")
        print()


def get_components(cells):
    cells = set(cells)
    if not cells:
        return []

    visited = set()
    components = []

    for start in cells:
        if start in visited:
            continue

        queue = deque([start])
        visited.add(start)
        comp = [start]

        while queue:
            x, y = queue.popleft()

            for dx, dy in dxy:
                nx, ny = x + dx, y + dy

                if (nx, ny) not in cells:
                    continue
                if (nx, ny) in visited:
                    continue

                comp.append((nx, ny))
                visited.add((nx, ny))
                queue.append((nx, ny))

        components.append(comp)

    return components


def adjacent_group(position):
    adjacent = set()

    for x, y in position:
        cur_group = position[(x, y)]

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            neighbor_group = position.get((nx, ny))

            if neighbor_group is None:
                continue
            if neighbor_group == cur_group:
                continue

            adjacent.add(frozenset((cur_group, neighbor_group)))

    return adjacent


def remove_divided_group(group_id, micro_group, position):
    components = get_components(micro_group[group_id])

    if len(components) <= 1:
        return

    removed = micro_group[group_id]
    micro_group[group_id] = set()

    for x, y in removed:
        if position.get((x, y)) == group_id:
            del position[(x, y)]


def normalize_shape(cells):
    min_x = min(x for x, y in cells)
    min_y = min(y for x, y in cells)
    return {(x - min_x, y - min_y) for x, y in cells}


def main():
    N, Q = map(int, input().split())
    # grid = [[0] * N for _ in range(N)]
    micro_group = defaultdict(set)
    position = {}

    for q in range(1, Q + 1):
        # print(f"=== {q} ===")
        r1, c1, r2, c2 = map(int, input().split())

        # 1. 미생물 투입
        affected = set()

        for i in range(r1, r2):
            for j in range(c1, c2):
                prev = position.get((i, j), 0)

                # 기존에 있던 다른 그룹이 덮이면 제거
                if prev and prev != q:
                    micro_group[prev].discard((i, j))
                    affected.add(prev)

                micro_group[q].add((i, j))
                position[(i, j)] = q
                # grid[i][j] = q

        # 덮여서 영향받은 기존 그룹들만 연결성 검사
        for group_id in affected:
            if not micro_group[group_id]:
                continue

            remove_divided_group(group_id, micro_group, position)

        # print(micro_group)
        # print(position)

        # 2. 배양 용기 이동
        # 영역 넓이 큰 순서대로 -> 먼저 투입된 번호 순
        large_area = sorted(
            [group_id for group_id, cells in micro_group.items() if cells],
            key=lambda group_id: (-len(micro_group[group_id]), group_id)
        )
        # print(large_area)

        # 새로운 배양용기에 (0, 0)부터 밀어넣기
        new_micro_group = defaultdict(set)
        new_position = {}

        for group_id in large_area:
            shape = normalize_shape(micro_group[group_id])  # (0, 0) 기준으로 변경

            placed = False
            for base_x in range(N):
                for base_y in range(N):
                    moved = {(base_x + dx, base_y + dy) for dx, dy in shape}

                    # 범위 체크
                    if any(not (0 <= x < N and 0 <= y < N) for x, y in moved):
                        continue

                    # 겹침 체크
                    if any((x, y) in new_position for x, y in moved):
                        continue

                    # 배치 성공
                    new_micro_group[group_id] = moved
                    for coord in moved:
                        new_position[coord] = group_id

                    placed = True
                    break
                if placed:
                    break

            # 어디에도 못 놓으면 제거
            if not placed:
                new_micro_group[group_id] = set()

        micro_group = new_micro_group
        position = new_position

        # 3. 결과 측정
        # 인접한 무리 쌍 찾기
        adj_group = adjacent_group(position)
        # print(adj_group)

        # 결과 계산하기
        score = 0
        for pair in adj_group:
            a, b = tuple(pair)
            score += len(micro_group[a]) * len(micro_group[b])

        print(score)


if __name__ == "__main__":
    # position = {(2, 2): 3, (2, 3): 2, (2, 4): 2, (2, 5): 2, (3, 2): 3, (3, 3): 2, (3, 4): 2, (3, 5): 2, (4, 2): 3, (4, 3): 2, (4, 4): 2, (4, 5): 2, (2, 6): 2, (2, 7): 2, (3, 6): 2, (3, 7): 2, (4, 6): 2, (4, 7): 2, (2, 0): 3, (2, 1): 3, (3, 0): 3, (3, 1): 3, (4, 0): 3, (4, 1): 3}
    # print(adjacent_group(position, 2, 2))
    main()
