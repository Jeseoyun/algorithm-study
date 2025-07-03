from collections import Counter

N = int(input())
number = [int(input()) for _ in range(N)]

freq = Counter(number)

max_freq = 0
max_freq_num = 0

for num in sorted(freq):
    if max_freq < freq[num]:
        max_freq = freq[num]
        max_freq_num = num

print(max_freq_num)