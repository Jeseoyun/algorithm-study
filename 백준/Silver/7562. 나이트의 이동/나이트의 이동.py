from collections import deque


dxy = [(-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2), (1, -2), (-1, -2)]


def bfs(board_size, start, destination):
    queue = deque()
    visited = set()
    queue.append((start, 1))
    visited.add(start)

    while queue:
        (x, y), cnt = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= board_size or ny < 0 or ny >= board_size:
                continue
            if (nx, ny) in visited:
                continue
            if (nx, ny) == destination:
                return cnt

            queue.append(((nx, ny), cnt+1))
            visited.add((nx, ny))


def main():
    T = int(input())

    for _ in range(T):
        I = int(input())
        start = tuple(map(int, input().split()))
        destination = tuple(map(int, input().split()))

        if start == destination:
            print(0)
        else:
            move_cnt = bfs(I, start, destination)
            print(move_cnt)


if __name__ == '__main__':
    main()