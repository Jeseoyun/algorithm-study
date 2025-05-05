def is_possible(points, c, min_dist):
    # 무조건 첫 번째 집에 설치해놓고 최소 거리만큼 벌려가면서 설치 가능한지만 확인
    installed = [points[0]]

    for idx in range(1, len(points)):
        # print(idx, installed)
        if points[idx] - installed[-1] >= min_dist:
            installed.append(points[idx])

        if len(installed) >= c:
            # print("갓챠~!", installed)
            return True

    return False


def main():
    N, C = map(int, input().split())  # 집 수, 공유기 수
    house_pos = [int(input()) for _ in range(N)]
    house_pos = sorted(house_pos)

    left = 1  # 가능한 최소 거리
    right = house_pos[-1] - house_pos[0]  # 가능한 최대 거리
    answer = 1

    while left <= right:
        mid = (left + right) // 2  # 시도 할 최소 거리
        # print("mid:", mid)

        if is_possible(house_pos, C, mid):  # C개의 공유기 설치 가능
            answer = mid
            left = mid + 1  # 더 넓은 거리도 가능한 지 확인

        else:  # 공유기 C개 설치 불가능
            right = mid - 1  # 더 좁은 거리는 가능한 지 확인

    print(answer)


if __name__ == "__main__":
    main()