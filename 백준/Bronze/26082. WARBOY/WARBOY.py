A, B, C = map(int, input().split())
enemy_ppc = int(B/A)

warboy_ppc = enemy_ppc*3
warboy_p = warboy_ppc*C

print(warboy_p)