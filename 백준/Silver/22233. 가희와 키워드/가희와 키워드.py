def main():
    N, M = map(int, input().split())
    keywords = set(input() for _ in range(N))

    for _ in range(M):
        memos = set(input().split(","))
        keywords -= memos
        print(len(keywords))


if __name__ == "__main__":
    main()
