def honey_comb(arr, max_honey, idx, comb, combs):
    # 꿀통 합이 C 넘기면 아예 저장 안함
    if sum(comb) > max_honey:
        return
     
    if len(arr) == idx:
        combs.append(comb[:])
        return comb[:]
    
    # 포함 하는 경우
    honey_comb(arr, max_honey, idx+1, comb + [arr[idx]], combs)
    # 포함 안하는 경우
    honey_comb(arr, max_honey, idx+1, comb, combs)


def cal_max_profit(combs):
    max_profit = 0

    for comb in combs:
        max_profit = max(max_profit, sum((i**2 for i in comb)))

    return max_profit


def main():
    T = int(input())

    for test_case in range(1, T+1):

        N, M, C = map(int, input().split())
        beehive = [list(map(int, input().split())) for _ in range(N)]

        max_profit = 0 

        # 1. 벌통 영역 선택
        for a_i in range(N):
            for a_j in range(N - M + 1):
                worker_A = beehive[a_i][a_j:a_j+M]
                
                # 2-1. A 꿀통 채취
                # 영역 내에서 꿀을 채취할 수 있는 모든 경우의 수를 구하고
                # 꿀 양의 합이 C를 넘지 않는 시점에서 최댓값
                a_combs = []
                honey_comb(worker_A, C, 0, [], a_combs)
                a_profit = cal_max_profit(a_combs)

                for b_i in range(a_i, N):
                    for b_j in range(N-M+1):
                        # A와 B가 같은 줄일 때 A랑 B랑 일이 겹치면 안됨
                        # -> B의 시작 지점이 A가 끝난 이후가 될 수 있도록 함
                        if a_i == b_i and a_j+M > b_j:
                            continue

                        worker_B = beehive[b_i][b_j:b_j+M]

                        # 2-2. B 꿀통 채취
                        b_combs = []
                        honey_comb(worker_B, C, 0, [], b_combs)

                        # print("꿀통 리밋:",C)
                        # print(a_combs, b_combs)

                        # 3. 수익 계산 -> 최댓값 찾기
                        b_profit = cal_max_profit(b_combs)
                        max_profit = max(a_profit + b_profit, max_profit)
            
        print(f"#{test_case} {max_profit}")


if __name__ == "__main__":
    main()
