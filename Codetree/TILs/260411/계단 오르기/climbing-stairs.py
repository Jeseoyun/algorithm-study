def main():
    N = int(input())
    step = [0]*(N+1)

    step[2] = 1
    
    if N >= 3:
        step[3] = 1
    
    for i in range(4, N+1):
        step[i] = step[i-2] + step[i-3]
    
    print(step[N]%10007)


if __name__ == "__main__":
    main()