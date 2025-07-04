def main():
    N, M, L, K = map(int, input().split())
    star_poo = [tuple(map(int, input().split())) for _ in range(K)]

    # 1. 최대한 많은 별똥별을 튕겨낼 수 있는 범위를 구한다
    # (1차 시도) 트램펄린을 만들 수 있는 가능한 모든 조합 구하기 => 메모리 초과
    # tp_pos = []
    # for tx in range(N-L+1):
    #     for ty in range(M-L+1):
    #         tp_pos.append((tx, ty))

    # (2차시도) 트램펄린 시작 지점을 별똥별이 있는 지점으로 설정
    # -> 최소 1개의 별똥별 무조건 포함
    # 틀림. 시작 지점이 무조건 별이 있는 지점일 필요가 없다.

    # # (3차 시도) 시작 지점의 범위를 찾아내야 한다.
    # # 딱 그 좌표에서부터 시작하는게 아니라 x 범위에서 최솟값이 되는 부분이 시작점의 x좌표가 될 수 있게
    # tx_candidate = set()
    # for sx, _ in star_poo:
    #     if 0 <= sx <= N-L:
    #         tx_candidate.add(sx)  # 트램펄린의 가장 상단이 별똥별 위치인 경우
    #     if 0 <= sx - L <= N-L:
    #         tx_candidate.add(sx-L)  # 트램펄린의 가장 하단이 별똥별 위치
    #
    # ty_candidate = set()
    # for _, sy in star_poo:
    #     if 0 <= sy <= M-L:
    #         ty_candidate.add(sy)  # 트램펄린 왼쪽 끝 지점이 별똥별 위치
    #     if 0 <= sy - L <= M-L:
    #         ty_candidate.add(sy-L)  # 트램펄린 오른쪽 끝 지점이 별똥별 위치

    # 2. 튕겨내지 못한 별똥별 개수를 구한다
    # max_sp = 0
    # for tx in tx_candidate:
    #     for ty in ty_candidate:
    #         curr_sp = 0
    #         for sx, sy in star_poo:
    #             if tx <= sx <= tx + L and ty <= sy <= ty + L:
    #                 curr_sp += 1
    #         max_sp = max(max_sp, curr_sp)

    # (4차시도) 두 점을 선택해서 두 점을 모두 포함할 수 있는 점을 가장 왼쪽 상단의 모서리로 잡기
    max_sp = 0
    for fx, fy in star_poo:
        for sx, sy in star_poo:
            curr_sp = 0
            for px, py in star_poo:
                if fx <= px <= fx + L and sy <= py <= sy + L:
                    curr_sp += 1
            max_sp = max(max_sp, curr_sp)

    print(K-max_sp)


if __name__ == "__main__":
    main()