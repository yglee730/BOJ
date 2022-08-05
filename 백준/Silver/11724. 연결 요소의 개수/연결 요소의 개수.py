import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
graph[0] = [0,0]
visited = [False for _ in range(N+1)]

cnt = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

    graph[a].sort()
    graph[b].sort()
    
def DFS(graph, start, visited):
    visited[start] = True 
    
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

for i in range(1, len(visited)):
    if visited[i] == False:
        cnt += 1
        DFS(graph, i, visited)
print(cnt)
