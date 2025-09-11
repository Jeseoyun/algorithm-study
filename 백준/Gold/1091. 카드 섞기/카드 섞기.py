def shuffle(current, S):
    shuffled = [0] * len(current)
    for i in range(len(current)):
        shuffled[i] = current[S[i]]
    #
    # print("원", current)
    # print("섞", shuffled)

    return shuffled


def main():
    N = int(input())
    P = list(map(int, input().split()))  # 목표
    S = list(map(int, input().split()))  # 카드 섞기

    current = [i for i in range(N)]
    original = current[:]

    cnt = 0

    while True:
        if [card%3 for idx, card in enumerate(current)] == P:
            print(cnt)
            break

        current = shuffle(current, S)
        # print(current)

        if current == original:
            print(-1)
            break

        cnt += 1


if __name__ == "__main__":
    main()