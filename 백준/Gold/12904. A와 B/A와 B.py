def main():
    S = input()
    T = list(input())

    while len(T) > len(S):
        if T[-1] == 'A':
            T.pop()
        else:
            T.pop()
            T.reverse()
            
    
    print(1 if ''.join(T) == S else 0)


if __name__ == "__main__":
    main()