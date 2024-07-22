def palindrome(input_str, i, j):
    if i>=j:
        return 1
    if input_str[i]!= input_str[j]:
        return 0
    else:
        return palindrome(input_str, i+1, j-1)


def main():
    t = int(input())

    for test_case in range(1, t+1):
        input_str = input()
        result = palindrome(input_str, 0, len(input_str)-1)
        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()