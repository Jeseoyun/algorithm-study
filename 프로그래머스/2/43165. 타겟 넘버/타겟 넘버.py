'''
dfs 로 구현
-> 이유: 모든 경우의 수를 탐색해서 가장 마지막 단계에서 결과를 얻어야 함
'''

def calculate_dfs(numbers, target, current_idx, calculated):
    # 종료 조건: numbers의 모든 값에 대해 연산이 종료
    # -> current_idx 값이 numbers인덱스 마지막 값을 넘게됨
    if current_idx == len(numbers):
        if target == calculated:
            return 1
        else:
            return 0
    
    # 경우의 수 2가지 -> 현재 상태에서 값을 더하는 경우와 빼는 경우
    cal_add = calculate_dfs(numbers, target, current_idx+1, calculated+numbers[current_idx])
    cal_sub = calculate_dfs(numbers, target, current_idx+1, calculated-numbers[current_idx])
    
    return cal_add + cal_sub


def solution(numbers, target):
    target_count = 0
    
    # 재귀호출 중단할 파라미터: current_idx
    # 누적해서 결과를 가져갈 파라미터: calculated
    # 조건을 충족하는 결과 개수를 저장할 파라미터: target_count
    target_count += calculate_dfs(numbers, target, 0, 0)
    
    return target_count