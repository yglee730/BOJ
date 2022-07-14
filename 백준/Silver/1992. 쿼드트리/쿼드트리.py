import sys
N = int(sys.stdin.readline())
img = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def QuadTree(x, y, N, comm):
    check = img[x][y]
    # print(x,y,N,comm)
    for i in range(x, x+N):
        for j in range(y, y+N):
            if check != img[i][j]:
                print('(', end='')
                QuadTree(x,y,N//2,"=> 왼쪽 위")
                QuadTree(x,y+N//2,N//2,"=> 오른쪽 위")
                QuadTree(x+N//2,y,N//2,"=> 왼쪽 아래")
                QuadTree(x+N//2,y+N//2,N//2,"=> 오른쪽 아래")
                print(')', end='')
                return
    if check == 0:
        print('0',end='')
        return
    else:
        print('1',end='')
        return

QuadTree(0,0,N, "=> main")