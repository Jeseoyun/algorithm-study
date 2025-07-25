def dfs(n, m, arr, step, curr, result):
    if step == m:
        result.append(curr)
        return

    for idx in range(n):
        if arr[idx] in set(curr):
            continue
        dfs(n, m, arr, step+1, curr+[arr[idx]], result)



def main():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    result = []
    dfs(N, M, arr, 0, [], result)

    for res in result:
        print(*res)


if __name__ == "__main__":
    main()