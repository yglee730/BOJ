N = int(input())
M = int(input())
material = list(map(int, input().split()))
material.sort()

cnt = 0

i = 0
j = len(material) - 1

while i != j:
    if (material[i] + material[j]) == M:
        cnt += 1
        j -= 1
    elif (material[i] + material[j]) < M:
        i += 1
    elif (material[i] + material[j]) > M:
        j -= 1
    
print(cnt)