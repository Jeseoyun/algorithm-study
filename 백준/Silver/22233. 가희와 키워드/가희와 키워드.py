def main():
    N, M = map(int, input().split())
    keywords = set(input() for _ in range(N))

    out = []
    for _ in range(M):
        memos = set(input().split(","))
        keywords -= memos
        out.append(len(keywords))

    print(*out, sep="\n")


if __name__ == "__main__":
    main()
