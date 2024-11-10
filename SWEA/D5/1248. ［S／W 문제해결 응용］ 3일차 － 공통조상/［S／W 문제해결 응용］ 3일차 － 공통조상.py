from collections import defaultdict, deque


def dfs(curr, parents):
    # 루트 노드일 경우 순회 종료
    if curr in child_patent.keys():
        parents.append(child_patent[curr])
        dfs(child_patent[curr], parents)
    else:
        return parents


T = int(input())

for test_case in range(1, T+1):
    V, E, v1, v2 = map(int, input().split())

    edges = list(map(int, input().split()))

    parent_child = defaultdict(list)
    child_patent = defaultdict(int)

    for i in range(0, len(edges), 2):
        parent = edges[i]
        child = edges[i+1]

        parent_child[parent].append(child)
        child_patent[child] = parent

    # 1. 각 정점에 대해 조상 리스트 구하기
    v1_parents, v2_parents = [v1], [v2]

    dfs(v1, v1_parents)
    dfs(v2, v2_parents)

    # 2. 공통 조상 찾기
    same_parent = 0
    for v_cmp in v1_parents:
        if v_cmp in v2_parents:
            same_parent = v_cmp
            break

    # 3. 공통 조상의 subtree 개수 찾기
    queue = deque()
    subtree = []
    queue.append(same_parent)
    subtree.append(same_parent)

    while queue:
        parent = queue.popleft()

        for child in parent_child[parent]:
            queue.append(child)
            subtree.append(child)

    print(f"#{test_case} {same_parent} {len(subtree)}")
