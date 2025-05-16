from collections import defaultdict, deque


def get_city_info(city, city_size):
    city_info = defaultdict(list)

    for i in range(city_size):
        for j in range(city_size):
            if city[i][j] == 1:
                city_info["house"].append((i, j))
            elif city[i][j] == 2:
                city_info["chicken"].append((i, j))

    return city_info


def comb(idx, curr, results, candidates, max_candidate):
    # print(idx, curr, results)
    if len(curr) > max_candidate:
        return

    if idx == len(candidates):
        if 1<= len(curr) <= max_candidate:
            results.append(curr[:])
        return

    comb(idx+1, curr+[candidates[idx]], results, candidates, max_candidate)
    comb(idx+1, curr, results, candidates, max_candidate)


def get_chicken_distance(house_pos, chicken_pos):
    total_chicken_dist = 0

    for hx, hy in house_pos:
        min_dist = float('inf')
        for cx, cy in chicken_pos:
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist)
        total_chicken_dist += min_dist

    return total_chicken_dist


def main():
    N, M = map(int, input().split())

    city = [list(map(int, input().split())) for _ in range(N)]
    # print(city)
    city_info = get_city_info(city, N)
    # print(f"city_info: {city_info}")

    # 1. 살아남은 치킨집 쌍 구하기
    survived = []
    comb(0, [], survived, city_info["chicken"], M)
    # print(survived)

    # 2. 치킨거리 구하기
    min_chicken_dist = float('inf')
    for chicken_comb in survived:
        dist = get_chicken_distance(city_info["house"], chicken_comb)
        min_chicken_dist = min(min_chicken_dist, dist)
        # print(min_chicken_dist, dist)

    print(min_chicken_dist)



if __name__ == "__main__":
    main()