def group_word_checker(word):
    exist = set()
    for idx, w in enumerate(word):
        if w not in exist:
            exist.add(w)
        else:
            if idx > 0 and word[idx-1] == w:
                continue
            else:
                return False
    return True


def main():
    N = int(input())

    result = 0
    for _ in range(N):
        word = input()
        if group_word_checker(word):
            result += 1

    print(result)


if __name__ == "__main__":
    main()