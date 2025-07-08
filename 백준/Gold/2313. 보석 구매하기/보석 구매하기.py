INF = float('inf')

# dp 이용
def main():
    n = int(input())

    max_gem_value = 0
    max_gem_idx = []

    for line in range(n):
        gn = int(input())
        gem_values = list(map(int, input().split()))

        start_idx = 0
        current_max = -INF

        max_value = -INF
        max_idx = []

        for i in range(gn):
            if current_max + gem_values[i] > gem_values[i]:
                current_max += gem_values[i]
            else:
                current_max = gem_values[i]
                start_idx = i

            if current_max > max_value:
                max_value = current_max
                max_idx = [(start_idx, i)]
            elif current_max == max_value:
                max_idx.append((start_idx, i))

        max_gem_value += max_value

        min_len = INF
        for s_idx, e_idx in max_idx:
            min_len = min(min_len, e_idx-s_idx+1)

        min_length_idx = [idx for idx in max_idx if idx[1]-idx[0]+1==min_len]
        # print(min_length_idx)

        max_gem_idx.append(sorted(min_length_idx, key=lambda x: (x[0], x[1]))[0])

    print(max_gem_value)
    for idx in max_gem_idx:
        print(*map(lambda x: x + 1, idx))


if __name__ == "__main__":
    main()