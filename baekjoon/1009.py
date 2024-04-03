T = int(input())

result = []

for _ in range(T):
    a, b = map(int, input().split())
    a %= 10  # a를 일의 자리로 만듦
    if a == 0:
        result.append(10)  # 0^b의 경우 마지막 자리는 10이다.
    else:
        b %= 4  # 주기성에 따라 b를 4로 나눈 나머지 값만 필요하다.
        if b == 0: b = 4  # b가 4의 배수일 경우 주기성에 따라 나머지가 0이 되므로, 4로 바꿔준다.
        result.append((a**b) % 10)

for num in result:
    print(num)