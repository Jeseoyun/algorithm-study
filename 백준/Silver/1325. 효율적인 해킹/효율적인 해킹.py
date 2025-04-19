import sys
from collections import deque
input = sys.stdin.readline

def count_hackable(start, graph):
    visited = [False] * len(graph)
    visited[start] = True
    queue = deque([start])
    count = 1  # 자기 자신 포함
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
                
    return count

def main():
    N, M = map(int, input().split())
    
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        A, B = map(int, input().split())
        graph[B].append(A)  # B를 해킹하면 A도 해킹할 수 있음
    
    max_count = 0
    counts = [0] * (N+1)
    
    for i in range(1, N+1):
        counts[i] = count_hackable(i, graph)
        max_count = max(max_count, counts[i])
    
    result = []
    for i in range(1, N+1):
        if counts[i] == max_count:
            result.append(i)
    
    print(*result)

if __name__ == "__main__":
    main()