
def main():
    s = input()
    target = input()

    m = len(target)
    target_list = list(target)

    stack = []

    for ch in s:
        stack.append(ch)

        if len(stack) < m:
            continue

        # print(stack[-m:])

        if stack[-m:] == target_list:
            # stack = stack[:-m]
            del stack[-m:]

        # print(stack)

    result = "".join(stack)
    print(result or "FRULA")


if __name__ == "__main__":
    main()


# def check_bomb_pos(org, cmp):
#     bomb_pos = set()
#
#     for i in range(len(org)):
#         sub = org[i:i+len(cmp)]
#
#         if sub == cmp:
#             bomb_pos.add((i, i+len(cmp)))
#
#     return bomb_pos
#
#
# def remove_bomb_str(org, bomb_pos):
#     org = list(org)
#
#     for pos in bomb_pos:
#         # print(pos)
#         for i in range(pos[0], pos[1]):
#             # print(i, org[i])
#             org[i] = "*"
#
#     org = "".join(org)
#     return org.replace("*", "")
#
#
# def main():
#     input_str = input()
#     target_str = input()
#
#     while True:
#         bomb_pos = check_bomb_pos(input_str, target_str)
#         # print(bomb_pos)
#
#         if not bomb_pos:
#             break
#
#         input_str = remove_bomb_str(input_str, bomb_pos)
#         # print(input_str)
#
#     print(input_str or "FRULA")
#
#
# if __name__ == "__main__":
#     main()