def main():
    N, M = map(int, input().split())

    book_weights = list(map(int, input().split())) if N > 0 else []

    weight_sum = 0
    box_cnt = 0
    for weight in book_weights:
        weight_sum += weight

        if weight_sum > M:
            box_cnt += 1
            weight_sum = weight
        elif weight_sum == M:
            box_cnt += 1
            weight_sum = 0

        # print(weight, weight_sum, box_cnt)

    if weight_sum > 0:
        box_cnt += 1

    print(box_cnt)


if __name__ == "__main__":
    main()
