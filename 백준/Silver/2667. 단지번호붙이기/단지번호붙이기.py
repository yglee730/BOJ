from collections import deque

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x,y))

    # print('queue:',queue)
    
    graph[x][y] = 0
    count = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    return count

num = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            num.append(BFS(i,j))

print(len(num))
num.sort()
for i in num:
    print(i)
