a = int(input())
b = list(map(int, input().split()))

if a == 1:
    print(b[0] ** 2)
elif a > 1:
    min_b = min(b)
    max_b = max(b)
    result = min_b * max_b
    print(result)