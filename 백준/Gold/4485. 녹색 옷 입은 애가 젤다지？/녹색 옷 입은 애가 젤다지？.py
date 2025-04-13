import heapq


def dijkstra(matrix, matrix_size, sx, sy):
    queue = [(matrix[sx][sy], sx, sy)]
    visited = [[float('inf')]*matrix_size for _ in range(matrix_size)]
    visited[sx][sy] = matrix[sx][sy]
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        cost, x, y = heapq.heappop(queue)

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= matrix_size or ny < 0 or ny >= matrix_size:
                continue

            if visited[nx][ny] > cost + matrix[nx][ny]:
                new_cost = cost + matrix[nx][ny]
                visited[nx][ny] = new_cost
                heapq.heappush(queue, (new_cost, nx, ny))

    return visited[matrix_size-1][matrix_size-1]


def main():
    prob_num = 1

    while True:
        N = int(input())
        cave_map = []

        if N == 0:
            break

        for _ in range(N):
            cave_map.append(list(map(int, input().split())))

        min_cost = dijkstra(cave_map, N, 0, 0)
        print(f"Problem {prob_num}: {min_cost}")
        prob_num += 1


if __name__ == "__main__":
    main()