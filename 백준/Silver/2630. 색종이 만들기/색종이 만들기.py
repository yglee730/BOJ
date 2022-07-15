import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

ans = []

def cutPaper(x, y, N):
    check = board[x][y]
    
    for i in range(x, x+N):
        for j in range(y, y+N):
            if check != board[i][j]:
                cutPaper(x,y,N//2)
                cutPaper(x,y+N//2,N//2)
                cutPaper(x+N//2, y, N//2)
                cutPaper(x+N//2, y+N//2, N//2)
                return
    if check == 1:
        ans.append(1)
    elif check == 0:
        ans.append(0)
        
cutPaper(0,0,N)
print(ans.count(0))
print(ans.count(1))