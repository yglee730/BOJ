arrK = []
SUCCESS = False

for i in range(9):
    arrK.append(int(input()))

for i in range(9):
    for j in range(i+1, 9):
        if (sum(arrK) - (arrK[i] + arrK[j])) == 100:
            n1, n2 = arrK[i], arrK[j]
            arrK.remove(n1)
            arrK.remove(n2)
            arrK.sort()
            SUCCESS = True
            break
    
    if SUCCESS == True:
        break
    
for i in range(len(arrK)):
    print(arrK[i])