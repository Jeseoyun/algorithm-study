import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(heap, -x)
    elif x == 0:
        print(-heapq.heappop(heap) if heap else 0)