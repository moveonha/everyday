N = int(input())  # 끝말잇기 기록의 개수
records = [input() for _ in range(N)]  # 끝말잇기 기록들을 리스트에 저장

M = int(input())  # 후보 단어의 개수
candidates = [input() for _ in range(M)]  # 후보 단어들을 리스트에 저장

# 가능한 후보들을 찾아서 저장
possible_candidates = []

for candidate in candidates:
    for record in records:
        if record == "?":
            continue
        if record[-1] == candidate[0]:
            possible_candidates.append(candidate)
            break

# 가능한 후보 중 첫 번째 후보를 출력
print(possible_candidates[0])
