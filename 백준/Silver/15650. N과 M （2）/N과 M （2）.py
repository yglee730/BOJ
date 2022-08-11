N, M = map(int, input().split())

arr = []

def DFS(start):
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return

    for i in range(start, N+1):
        if i not in arr:
            arr.append(i)
            DFS(i+1)
            arr.pop()
DFS(1)