def main():
    board = input().strip()

    board = board.replace("XXXX", "AAAA")
    board = board.replace("XX", "BB")

    if "X" in board:
        print(-1)
    else:
        print(board)


if __name__ == "__main__":
    main()
