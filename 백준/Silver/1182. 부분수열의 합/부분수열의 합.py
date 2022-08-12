N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

def DFS(idx, arrSum):
    global cnt

    if idx >= N:
        return
    
    arrSum += arr[idx]
    
    if S == arrSum:
        cnt += 1

    DFS(idx+1, arrSum-arr[idx])
    DFS(idx+1, arrSum)

DFS(0, 0)
print(cnt)