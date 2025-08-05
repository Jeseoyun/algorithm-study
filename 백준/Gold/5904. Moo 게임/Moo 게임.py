def moo_game(lengths, n, k):
    if k == 0:
        return "moo"[n-1]

    prev_len = lengths[k-1]
    mid_len = k+3

    if n <= prev_len:
        return moo_game(lengths, n, k-1)
    elif n <= prev_len + mid_len:
        if n - prev_len == 1:
            return "m"
        else:
            return "o"
    else:
        return moo_game(lengths, n-prev_len-mid_len, k-1)


def main():
    N = int(input())

    lengths = [3]
    k=1

    while lengths[-1] < N:
        k = len(lengths)
        lengths.append(lengths[-1]*2 + (k+3))

    nth_word = moo_game(lengths, N, k)
    print(nth_word)


if __name__ == "__main__":
    main()