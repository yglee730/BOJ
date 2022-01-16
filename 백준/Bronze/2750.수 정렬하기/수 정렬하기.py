N = int(input())
arrN = []

for i in range(N):
    arrN.append(int(input()))
    
for i in range(len(arrN)):
    for j in range(len(arrN)):
        if arrN[i] < arrN[j]:
            arrN[i], arrN[j] = arrN[j], arrN[i]
    
for i in range(len(arrN)):
    print(arrN[i])