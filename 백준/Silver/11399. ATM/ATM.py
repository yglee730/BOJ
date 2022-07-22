N = int(input())
wait = list(map(int, input().split()))

ans = 0
li = []

for i in sorted(wait):
    ans += i
    li.append(ans)

print(sum(li))
