def main():
    N, M, A, B = map(int, input().split())

    time_table = list(map(int, input().split()))
    like = set(map(int, input().split()))
    dislike = set(map(int, input().split()))

    preference = 0
    streak = 0
    status = 0  # 1: like, -1: dislike, 0: neutral
    MIN_STREAK = 3

    for subject in time_table:
        # 1. 현재 상태 체크
        if subject in like:
            new_status = 1
        elif subject in dislike:
            new_status = -1
        else:
            new_status = 0

        # 2. 이전과 상태가 연속적인지 체크
        if new_status != status:
            # 연속적이지 않은데, 이전에 min_strick 이상 연속되었을 경우 선호도 업데이트
            if streak >= MIN_STREAK:
                preference += (streak * status)
            streak = 1
            status = new_status
        else:
            # 연속적이면 strick 업데이트
            streak += 1
    
    # 마지막 과목도 체크
    if streak >= MIN_STREAK:
        preference += (streak * status)

    print(preference)


if __name__ == "__main__":
    main()
