T = int(input())

result =[]

for _ in range(T):
    a, b = map(int, input().split())
    num = (a**b)%10
    if num == 0:
        result.append(10)
    else:
        result.append(num)
        
for num in result:
    print(num)