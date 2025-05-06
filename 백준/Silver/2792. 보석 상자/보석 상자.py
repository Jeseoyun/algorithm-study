import math


def is_possible(gems, students_num, max_given):
    total = 0

    for gem in gems:
        total += math.ceil(gem / max_given)  # 보석을 나눠줄 때 필요한 학생 수

    return total <= students_num


def main():
    N, M = map(int, input().split())  # 학생 수, 보석 종류 수
    gems = [int(input()) for _ in range(M)]

    left = 1
    right = max(gems)
    answer = max(gems)

    while left <= right:
        mid = (left + right) // 2

        if is_possible(gems, N, mid):  # 한 학생에게 최대 mid개까지 줘도 다 나눠줄 수 있을까?
            answer = mid
            right = mid - 1  # 더 적게 줘도 가능한지 확인
        else:
            left = mid + 1

    print(answer)


if __name__ == "__main__":
    main()