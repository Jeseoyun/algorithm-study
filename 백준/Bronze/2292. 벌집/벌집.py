def main():
    N = int(input())

    layer = 1  # 지나가는 방 개수 (겹 수)
    end = 1  # 현재 겹에서 마지막 번호

    while N > end:
        end += 6 * layer
        layer += 1

    print(layer)
    

if __name__ == "__main__":
    main()