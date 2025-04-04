import sys
input = sys.stdin.readline

N=int(input())
users = set()
total_count = 0

for _ in range(N):
    user_input = input().strip()
    if user_input == 'ENTER':
        total_count += len(users)
        users.clear()
    else:
        users.add(user_input)
total_count += len(users)
print(total_count)
