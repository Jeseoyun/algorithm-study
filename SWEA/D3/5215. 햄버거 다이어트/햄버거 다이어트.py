def best_diet_burger(idx, accum_kcal, accum_score):
    global max_score
    # 인덱스가 리스트 범위를 벗어나면 종료
    if idx == len(taste_kcal):
        if accum_kcal <= kcal_limit:
            max_score = max(max_score, accum_score)
        return
 
    # 현재 항목을 포함하지 않는 경우
    best_diet_burger(idx + 1, accum_kcal, accum_score)
 
    # 현재 항목을 포함하는 경우 (칼로리 제한 체크)
    if accum_kcal + taste_kcal[idx][1] <= kcal_limit:
        best_diet_burger(idx + 1, accum_kcal + taste_kcal[idx][1], accum_score + taste_kcal[idx][0])
 
 
T = int(input())
 
for test_case in range(1, T + 1):
    N, kcal_limit = map(int, input().split())
 
    taste_kcal = [list(map(int, input().split())) for _ in range(N)]
 
    max_score = 0
    best_diet_burger(0, 0, 0)  # 현재 idx, 누적kcal, 누적만족도
 
    print(f"#{test_case} {max_score}")