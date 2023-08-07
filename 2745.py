def base_conversion(number, base):
    decimal_value = 0
    length = len(number)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(length):
        digit = number[length - 1 - i]
        decimal_value += digits.index(digit) * (base ** i)
    
    return decimal_value

# 입력 받기
input_data = input().split()
number = input_data[0]
base = int(input_data[1])

# 진법 변환 함수 호출
result = base_conversion(number, base)

# 결과 출력
print(result)
