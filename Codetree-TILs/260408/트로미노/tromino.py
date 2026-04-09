dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def possible_shape(x, y, N, M, _dxy):
    nx, ny = x + _dxy[0], y + _dxy[1]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        return False
    return True


def main():
    N, M = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for x in range(N):
        for y in range(M):
            # 1. L자 모양
            for i in range(4):
                if not possible_shape(x, y, N, M, dxy[i]):
                    continue
                if not possible_shape(x, y, N, M, dxy[(i+1)%4]):
                    continue
                
                dx1, dy1 = dxy[i]
                dx2, dy2 = dxy[(i+1)%4]
                max_sum = max(max_sum, blocks[x][y] + blocks[x+dx1][y+dy1] + blocks[x+dx2][y+dy2])
            
            # 2. I자 모양
            for i in range(2):
                if not possible_shape(x, y, N, M, dxy[i]):
                    continue
                if not possible_shape(x, y, N, M, dxy[i+2]):
                    continue
                
                dx1, dy1 = dxy[i]
                dx2, dy2 = dxy[i+2]
                max_sum = max(max_sum, blocks[x][y] + blocks[x+dx1][y+dy1] + blocks[x+dx2][y+dy2])

    print(max_sum)



if __name__ == "__main__":
    main()