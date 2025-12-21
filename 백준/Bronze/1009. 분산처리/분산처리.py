T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(pow(a,b,10) or 10)