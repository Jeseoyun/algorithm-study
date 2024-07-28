def check_diff(a, b):
    cnt = sum(1 for aa, bb in zip(a, b) if aa != bb)
    return cnt == 1


def change_char_dfs(words, target, visited, curr_idx, depth=0):
    # 탈출 조건: 현재 단어와 target 단어가 같을 때
    if words[curr_idx] == target:
        return depth
    
    min_depth = float('inf')
    for cmp_idx in range(len(words)):
        if check_diff(words[cmp_idx], words[curr_idx]) and not visited[cmp_idx]:
            visited[cmp_idx] = True
            min_depth = min(min_depth, change_char_dfs(words, target, visited, cmp_idx, depth+1))
            visited[cmp_idx] = False
    
    return min_depth


def solution(begin, target, words):
    # begin을 words의 첫 원소로 넣어 dfs 탐색
    words = [begin] + words
    visited = [False] * len(words)
    result = change_char_dfs(words, target, visited, 0)
    return result if result != float('inf') else 0