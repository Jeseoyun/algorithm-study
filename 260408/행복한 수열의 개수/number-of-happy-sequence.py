from collections import deque


dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def main():
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]

    happy = 0
    
    # 행 탐색
    for i in range(N):
        seq = 1
        found = False
        for j in range(N-1):
            if info[i][j] == info[i][j+1]:
                seq += 1
            else:
                if seq >= M:
                    found = True
                seq = 1

        if seq >= M:
            found = True

        if found:
            happy += 1
    
    # 열 탐색
    # 열 검사
    for j in range(N):
        seq = 1
        found = False

        for i in range(N-1):
            if info[i][j] == info[i+1][j]:
                seq += 1
            else:
                if seq >= M:
                    found = True
                seq = 1

        if seq >= M:
            found = True

        if seq >= M:
            happy += 1

    print(happy)


if __name__ == "__main__":
    main()
