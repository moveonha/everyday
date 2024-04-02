T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # 두 원이 동심원일 경우
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)  # 무한대의 점이 있음
        else:
            print(0)  # 만나지 않음
        continue

    # 두 원이 서로 만나지 않는 경우
    if r1 + r2 < d or max(r1, r2) > d + min(r1, r2):
        print(0)
    # 두 원이 한 점에서 만나는 경우
    elif r1 + r2 == d or max(r1, r2) == d + min(r1, r2):
        print(1)
    # 두 원이 두 점에서 만나는 경우
    else:
        print(2)