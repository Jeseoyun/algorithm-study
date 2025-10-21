from collections import deque
import math


def get_dist(a, b):
   return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def bfs(graph, starts, enemy, damage):
    queue = deque([])
    visited = set()
    total_damage = 0

    for start in starts:
        visited.add(start)
        queue.append((start, damage))  # (x, y), damage

    while queue:
        # print(queue, visited)
        node, damage = queue.popleft()
        total_damage += damage

        for adj in graph[node]:
            if adj in visited:
                continue

            if adj == tuple(enemy):
                continue

            queue.append((adj, damage/2))
            visited.add(adj)

    return total_damage


def main():
    N, R, D, *enemy = map(int, input().split())  # 탑 개수, 사정거리, 초기 에너지, 적의 좌표

    tower_graph = dict()
    tower_graph[tuple(enemy)] = set()

    for _ in range(N):
        x, y = map(int, input().split())
        tower_graph[(x, y)] = set()

    # 인접 노드 계산 -> 거리가 R 이내이면 인접함으로 간주
    for node in tower_graph.keys():
        for adj in tower_graph.keys():
            if node == adj:
                continue

            if get_dist(node, adj) <= R:
                tower_graph[node].add(adj)
                tower_graph[adj].add(node)

    print(bfs(tower_graph, tower_graph[tuple(enemy)], enemy, D))


if __name__ == "__main__":
    main()