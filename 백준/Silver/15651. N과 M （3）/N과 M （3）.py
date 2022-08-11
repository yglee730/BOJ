N, M = map(int, input().split())

arr = []

def DFS():
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return

    for i in range(1, N+1):
        arr.append(i)
        DFS()
        arr.pop()
DFS()