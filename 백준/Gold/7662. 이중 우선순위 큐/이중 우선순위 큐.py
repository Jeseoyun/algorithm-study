import heapq
from collections import defaultdict


def main():
    T = int(input())

    for _ in range(T):
        k = int(input())

        max_heap = []
        min_heap = []
        is_valid = defaultdict(int)
        for _ in range(k):
            oper, num = input().split()

            if oper == "I":
                heapq.heappush(max_heap, int(num)*-1)
                heapq.heappush(min_heap, int(num))
                is_valid[int(num)] += 1
            elif oper == "D" and num == "1":
                while max_heap:
                    val = -heapq.heappop(max_heap)
                    if is_valid[val] > 0:
                        is_valid[val] -= 1
                        break
            elif oper == "D" and num == "-1":
                while min_heap:
                    val = heapq.heappop(min_heap)
                    if is_valid[val] > 0:
                        is_valid[val] -= 1
                        break

        max_val = None
        while max_heap:
            val = -heapq.heappop(max_heap)
            if is_valid[val] > 0:
                max_val = val
                break

        min_val = None
        while min_heap:
            val = heapq.heappop(min_heap)
            if is_valid[val] > 0:
                min_val = val
                break

        if max_val is not None and min_val is not None:
            print(max_val, min_val)
        else:
            print("EMPTY")


if __name__ == "__main__":
    main()