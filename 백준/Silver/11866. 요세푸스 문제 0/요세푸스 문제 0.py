N, K = map(int, input().split())

list = [i for i in range(1, N+1)]
out = []

count = 1

while len(out) != N:
    Num = list.pop(0)
    
    if count == K:
        out.append(Num)
        count = 1
    else:
        list.append(Num)        
        count += 1

print('<', end='')
for i in range(len(out)-1):    
    print(out[i], end=', ')
print(out[len(out)-1],end='')
print('>',end='')