N = int(input())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
p = price[0]

for i in range(N-1):
    if p > price[i]:
        p = price[i]
    ans += p*roads[i]

print(ans)