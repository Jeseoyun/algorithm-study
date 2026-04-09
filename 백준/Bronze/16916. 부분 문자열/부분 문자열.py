import sys


def make_lps(pattern):
    lps = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps


def kmp(text, pattern):
    lps = make_lps(pattern)
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                return 1
            j += 1

    return 0


S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
print(kmp(S, P))