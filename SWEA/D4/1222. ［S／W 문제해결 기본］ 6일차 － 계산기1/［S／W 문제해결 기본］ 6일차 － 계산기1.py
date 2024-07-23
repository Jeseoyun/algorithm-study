def infix_to_postfix(infix):
    stack = []
    output = []

    for target in infix:
        if target.isdigit():
            if not stack:
                output.append(target)
            else:
                output.append(target)
                output.append(stack.pop())
        else:
            stack.append(target)

    return output


def calculate_postfix(postfix):
    stack = []
    for target in postfix:
        if target.isdigit():
            stack.append(target)
        elif target == "+":
            values = [stack.pop() for _ in range(len(stack))]
            val = sum(map(int, values))
            stack.append(val)
    result = stack.pop()
    return result


def main():
    # import sys
    # sys.stdin = open("input.txt", "r")

    for test_case in range(1, 11):
        length = int(input())
        infix = list(input())
        postfix = infix_to_postfix(infix)
        r = calculate_postfix(postfix)
        print(f"#{test_case} {r}")


if __name__ == "__main__":
    main()
