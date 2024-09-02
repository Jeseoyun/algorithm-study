def disjoint_set(adj_list, N):
    p = [i for i in range(N+1)]

    def find_set(x):
        if p[x] != x:
            p[x] = find_set(p[x])
        return p[x]
    
    def union(x, y):
        px = find_set(x)
        py = find_set(y)

        if px != py:
            if p[px] < p[py]:
                p[py] = px
            else:
                p[px] = py

    for start, end in adj_list:
        ps = find_set(start)
        pe = find_set(end)

        if ps != pe:
            union(start, end)
    
    for i in range(len(p)):
        find_set(i)

    return set(p[1:])


def main():
    T = int(input())

    for test_case in range(1, T+1):
        N, M = map(int, input().split())
        adj_list = [list(map(int, input().split())) for _ in range(M)]

        ds = disjoint_set(adj_list, N)

        print(f"#{test_case} {len(ds)}")


if __name__ == "__main__":
    main()