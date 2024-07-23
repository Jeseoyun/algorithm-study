# def set_laser(layout):
#     '''레이저가 있는 곳을 |로 표시'''
#     laser_layout = []
#     for idx in range(len(layout)):
#         if idx != 0 and layout[idx-1] == "(" and layout[idx] == ")":
#             laser_layout.pop()
#             laser_layout.append("|")
#         else:
#             laser_layout.append(layout[idx])
#     return laser_layout
#
#
# def iron_slice(layout):
#     '''레이저가 쇠막대기를 몇 개로 자르는지 반환'''
#     stack = []
#     iron_count = 0
#
#     for idx in range(len(layout)):
#         if layout[idx] == "(":  # 여는 괄호를 만났을 때
#             stack.append(idx)  # 여는 괄호의 위치를 스택에 추가
#         elif layout[idx] == ")":  # 닫힌 괄호를 만났을 때
#             start_idx = stack.pop()
#             laser_count = layout[start_idx:idx+1].count("|")
#             iron_count += (laser_count + 1)  # 나눠진 쇠막대기 개수는 여는 괄호와 닫힌 괄호 사이의 레이저 개수 + 1
#
#     return iron_count


def iron_slice(layout):
    stack = []
    iron_count = 0

    for idx in range(len(layout)):
        if layout[idx] == "(":  # 여는 괄호를 만났을 때
            stack.append("(")
        elif layout[idx] == ")":  # 닫힌 괄호를 만났을 때
            stack.pop()
            if layout[idx - 1] == "(":  # 레이저인 경우
                iron_count += len(stack)
            else:  # 쇠막대기 끝인 경우
                iron_count += 1

    return iron_count


def main():
    TC = int(input())

    for test_case in range(1, TC+1):
        layout = list(input())
        # laser_layout = set_laser(layout)
        result = iron_slice(layout)

        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()
