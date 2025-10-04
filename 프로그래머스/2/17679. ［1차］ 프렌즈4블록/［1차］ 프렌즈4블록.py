from collections import deque


def find_4blocks(board, cx, cy):
    if board[cx][cy] == board[cx+1][cy] == board[cx][cy+1] == board[cx+1][cy+1]:
        return ((cx, cy), (cx+1, cy), (cx, cy+1), (cx+1, cy+1))
    else:
        return ()

    
def remove_blocks(board, m, n, bombed_blocks):
    for x, y in bombed_blocks:
        board[x][y] = 0
        
    for j in range(n):
        column = [board[i][j] for i in range(m) if board[i][j]]
        
        while len(column) != m:
            column.insert(0, 0)
        
        for i in range(m):
            board[i][j] = column[i]
    

def solution(m, n, board):
    removed = 0
    
    for i in range(m):
        board[i] = list(board[i])
    
    while True:
        # 1. 부술 블록들 위치 찾기
        bombed_blocks = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == 0:
                    continue

                blocks = find_4blocks(board, i, j)
                # print(blocks)

                for block in blocks:
                    bombed_blocks.add(block)
        
        if not bombed_blocks:
            break
        else:
            removed += len(bombed_blocks)

        # 2. 부수고 밀어내기
        remove_blocks(board, m, n, bombed_blocks)
        # print(board)
        # break
    
    return removed