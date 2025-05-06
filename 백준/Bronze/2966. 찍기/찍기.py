guess = {
    "Adrian": "ABC",
    "Bruno": "BABC",
    "Goran": "CCAABB"
}

N = int(input())
answer = input()

gotcha = {name: 0 for name in guess.keys()}
for name in guess.keys():
    for idx in range(N):
        if answer[idx] == guess[name][idx % len(guess[name])]:
            gotcha[name] += 1

_max = 0
_max_name = []
for name in gotcha:
    if _max < gotcha[name]:
        _max = gotcha[name]
        _max_name = [name]
    elif _max == gotcha[name]:
        _max_name.append(name)

print(_max)
for name in sorted(_max_name):
    print(name)