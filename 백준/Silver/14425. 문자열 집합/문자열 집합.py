N, M = map(int, input().split())

S = {}
cnt = 0

for i in range(N):
    name = input()
    S[name] = hash(name)
    
for i in range(M):
    name2 = input()
    if name2 in S:
        cnt += 1
    
print(cnt)