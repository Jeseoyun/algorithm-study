def comb(idx, total):
    if idx == n:
        return 1 if total == s else 0
    # 현재 숫자 선택 X, 선택 O
    return comb(idx + 1, total) + comb(idx + 1, total + numbs[idx])


n, s = map(int, input().split())
numbs = list(map(int, input().split()))

# 공집합 제외
ans = comb(0, 0)
if s == 0:
    ans -= 1

print(ans)