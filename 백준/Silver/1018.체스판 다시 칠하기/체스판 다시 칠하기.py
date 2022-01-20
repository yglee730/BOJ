N, M = map(int, input().split())
chess = []
result = []

for i in range(N):
    chess.append(input())

for i in range(0,N-7):
    for j in range(0, M-7):
        isW = 0
        isB = 0
        for k in range(i, 8+i):
            for l in range(j, 8+j):
                if (k+l)%2 == 0:
                    if chess[k][l] != 'W': 
                        isB += 1        
                    if chess[k][l] != 'B': 
                        isW += 1          
                else:
                    if chess[k][l] != 'B':
                        isB += 1
                    if chess[k][l] != 'W':
                        isW += 1
        result.append(isW)
        result.append(isB)    
            
print(min(result))