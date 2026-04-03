from collections import deque

HIT = 1
MISS = 5


def solution(cacheSize, cities):
    cache = deque([])
    exec_time = 0
    
    if cacheSize == 0:
        return len(cities)*MISS
    
    for city in cities:
        city_cleaned = city.lower()
        
        if city_cleaned in cache:
            cache.remove(city_cleaned)
            cache.append(city_cleaned)
            exec_time += HIT
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city_cleaned)
            exec_time += MISS
        # print(city, cache)

    return exec_time