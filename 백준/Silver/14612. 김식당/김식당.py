def main():
    N, M = map(int, input().split())

    posts = []

    for _ in range(N):
        command, *args = input().split()
        args = list(map(int, args))

        if command == "order":
            posts.append((args[1], args[0]))  # 주문 시간, 테이블 번호

        elif command == "sort":
            posts.sort(key=lambda x: (x[0], x[1]))

        elif command == "complete":
            for i, (t, n) in enumerate(posts):
                if n == args[0]:
                    posts.pop(i)
                    break

        if posts:
            print(*(h[1] for h in posts), sep=" ")
        else:
            print("sleep")


if __name__ == "__main__":
    main()