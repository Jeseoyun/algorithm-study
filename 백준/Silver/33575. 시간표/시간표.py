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
        if subject in like:
            new_status = 1
        elif subject in dislike:
            new_status = -1
        else:
            new_status = 0

        if new_status != status:
            if streak >= MIN_STREAK:
                preference += (streak * status)
            streak = 1
            status = new_status
        else:
            streak += 1

    if streak >= MIN_STREAK:
        preference += (streak * status)

    print(preference)


if __name__ == "__main__":
    main()