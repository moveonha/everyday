N = int(input())
words =[]
candidates = []


for _ in range(N):
    word = str(input())
    words.append(word)

for i in range(len(words)):
    if words[i] == "?":
        print(i+1)
        answer = []
        answer.append(words[i-1])
        answer.append(words[i+1])

for i in range(i-1):
    candidate = str(input())
    candidates.append(candidate)
    
for i in range(N):
    if words[i] == candidates[i]:
        continue