def main():
    N, M = map(int, input().split())
    keywords = set(input() for _ in range(N))

    out = []
    append = out.append
    diff_update = keywords.difference_update

    for _ in range(M):
        line = input().rstrip()
        diff_update(line.split(","))   # set 만들지 말고 iterable 그대로
        append(str(len(keywords)))

    print(*out, sep="\n")


if __name__ == "__main__":
    main()
