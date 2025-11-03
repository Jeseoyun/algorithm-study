def triangle_area(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    return (x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3) * 0.5


def mid_point(points, N):
    mx = 0
    my = 0
    for x, y in points:
        mx += x
        my += y
    return mx / N, my / N


def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    mid = mid_point(points, N)
    area = 0.0
    for i in range(N):
        area += triangle_area(points[i], points[(i+1) % N], mid)

    print(f"{abs(area):.1f}")


if __name__ == "__main__":
    main()
