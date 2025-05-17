from bisect import bisect, bisect_right


def main():
    N, M = map(int, input().split())

    scouter = []

    for _ in range(N):
        grade, power = input().split()
        scouter.append([int(power), grade])

    scouter.sort(key=lambda x: x[0])

    result = []
    for _ in range(M):
        character_power = int(input())
        start = 0
        end = len(scouter)-1

        while start <= end:
            mid = (start + end) // 2

            if character_power > scouter[mid][0]:
                start = mid + 1
            else:
                end = mid - 1

        result.append(scouter[start][1])

    print(*result, sep='\n')
    

if __name__ == "__main__":
    main()