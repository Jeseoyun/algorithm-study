def solution(land):
    score = land[0][:]

    for i in range(1, len(land)):
        prev = score[:]
        for j in range(4):
            score[j] = land[i][j] + max(prev[k] for k in range(4) if k != j)

    return max(score)