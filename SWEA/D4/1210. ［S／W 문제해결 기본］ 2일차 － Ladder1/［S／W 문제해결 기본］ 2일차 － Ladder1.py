TEST_CASE = 10
LADDER_SIZE = 100
DESTINATION = 2


def search(arr, y, x, visited=None):
    if visited == None:
        visited = set()
    
    visited.add((y, x))  # 한 번 방문한 곳은 다시 방문하지 않음 -> 이거 설정 안하면 왼쪽-오른쪽 계속 순환하는 문제 발생
    
    if y == 0:  # 사다리의 최상단에서의 x값이 도착 지점으로 가는 입구가 됨
        return x
    if x > 1 and arr[y][x-1] == 1 and (y, x-1) not in visited:
        return search(arr, y, x-1, visited)  # 왼쪽으로 이동
    elif x < (LADDER_SIZE-1) and arr[y][x+1] == 1 and (y, x+1) not in visited:
        return search(arr, y, x+1, visited)  # 오른쪽으로 이동
    else:
        return search(arr, y-1, x, visited)  # 왼쪽, 오른쪽 모두 길이 없을 경우 위로 이동


def main():
    for _ in range(TEST_CASE):
        t = int(input())
        arr = [list(map(int, input().split())) for _ in range(LADDER_SIZE)]
        arrival_point = arr[-1].index(DESTINATION)  # 도착 지점: 사다리의 최하단에 2가 있는 곳
        
        # 도착 지점으로부터 위로 거슬러 올라감
        result = search(arr, LADDER_SIZE-2, arrival_point)  # 도착 지점 바로 위가 시작 지점이 됨

        print(f"#{t} {result}")


if __name__ == "__main__":
    main()