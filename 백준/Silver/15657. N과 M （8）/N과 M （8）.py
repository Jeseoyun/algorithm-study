def dfs(n, m, step, start, arr, curr, result):
    # print(curr)
    if step == m:
        result.append(curr)
        return

    for i in range(start, n):
        dfs(n, m, step+1, i, arr, curr+[arr[i]], result)


def main():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    result = []
    dfs(N, M, 0, 0, arr, [], result)


    for res in result:
        print(*res)


if __name__ == "__main__":
    main()