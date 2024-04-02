T = int(input())
Data = int(input())
for _ in range(T*2):
    for _ in range(Data):
        c = list(map(int,input().split()))

    K = int(input())
    for _ in range(K):
        y = list(map(int,input().split()))
print(T, K, c, y)