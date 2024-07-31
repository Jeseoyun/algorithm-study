class Counter:
    def __init__(self):
        self.cnt = 0

    def increase(self):
        self.cnt += 1


def subset_sum(arr, k, idx, subset, counter):
    if sum(subset) > k:
        return
    
    if idx == len(arr):
        if sum(subset) == k:
            counter.increase()
        return

    # 현재 원소를 포함 하거나
    subset_sum(arr, k, idx+1, subset+[arr[idx]], counter)

    # 현재 원소를 포함하지 않거나
    subset_sum(arr, k, idx+1, subset, counter)


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))

        result = Counter()
        subset_sum(arr, K, 0, [], result)

        print(f"#{test_case} {result.cnt}")


if __name__ == "__main__":
    main()