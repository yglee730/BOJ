N = int(input())
bulk = []
rank = []

cnt = 0

for i in range(N):
    w, h = map(int, input().split(' '))
    bulk.append([w, h])
    
for i in range(N):
    Weight, Height = bulk[i][0], bulk[i][1]
    for j in range(N):
        if (Weight < bulk[j][0]) and (Height < bulk[j][1]):
            cnt += 1
    rank.append(cnt+1)
    cnt = 0
    
for i in rank:
    print(i, end=' ')