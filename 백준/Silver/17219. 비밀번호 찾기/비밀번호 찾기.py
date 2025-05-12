from collections import defaultdict

N, M = map(int, input().split())

addr_pwd_dict = defaultdict(str)
for _ in range(N):
    addr, pwd = input().split()
    addr_pwd_dict[addr] = pwd

for _ in range(M):
    print(addr_pwd_dict[input()])
