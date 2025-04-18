def space_counter(matrix, min_size):
    result = 0
    for arr in matrix:
        # print(arr)
        if 'X' not in arr:
            if len(arr) >= min_size:
                result += 1
            continue
        elif '.' not in arr:
            continue

        cnt = 0
        for elem in arr:
            if elem == 'X':
                if  cnt >= min_size:
                    result += 1
                cnt = 0
            elif elem == '.':
                cnt += 1
            # print(elem, cnt, result)
        if cnt >= min_size:
            result += 1
    return result


def main():
    N = int(input())
    room = []

    MIN_SIZE = 2

    for _ in range(N):
        room.append([_ for _ in input()])

    row = space_counter(room, MIN_SIZE)
    col = space_counter(list(zip(*room)), MIN_SIZE)

    print(row, col)


if __name__ == "__main__":
    main()
