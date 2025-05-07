# def comb(idx, clothes, curr, res):
#     if idx == len(clothes):
#         if curr:
#             res[0] += 1
#         return
#
#     # 해당 종류 의상 착용하지 않았으면 착용 하거나
#     if clothes[idx][1] not in curr:
#         comb(idx+1, clothes, curr+[clothes[idx][1]], res)
#
#     # 착용하지 않거나
#     comb(idx+1, clothes, curr, res)


def main():
    test_case = int(input())

    for _ in range(test_case):
        n = int(input())
        clothes = [input().split() for _ in range(n)]

        wear = dict()
        for clothes_name, clothes_type in clothes:
            if clothes_type in wear:
                wear[clothes_type].append(clothes_name)
            else:
                wear[clothes_type] = [clothes_name]

        cnt = 1
        for clothes_type in wear:
            cnt *= (len(wear[clothes_type]) + 1)

        cnt -= 1
        print(cnt)


        # result = [0]
        # comb(0, clothes, [], result)
        # print(result[0])


if __name__ == "__main__":
    main()