N, K = map(int, input().split())
coin = []

for i in range(N):
    coin.append(int(input()))
    
coin.sort(reverse=True)

index = 0
cnt = 0
while K > 0:
    if K >= coin[index]:
        cnt += K // coin[index]
        K = K % coin[index]
    else:
        index += 1
    
print(cnt)