#초기 가방 설정
N , K = map(int, input().split())
baggage = []

#가방 설정 후 짐 무게, 가치 입력하기
for i in range(N):
    baggage.append(list(map(int,input().split())))
    
#모두 입력했으면 전체 합산하기
print(baggage)