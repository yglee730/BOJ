L, C = map(int, input().split())
arr = sorted(list(input().split()))

vowel = ['a','e','i','o','u']
ans = []

def DFS(cnt, idx):
    if L == cnt:
        #자음, 모음
        co, vo = 0, 0

        for i in range(L):
            if ans[i] in vowel:
                vo += 1
            else:
                co += 1
        
        if co >= 2 and vo >= 1:
            print("".join(ans))

        return
    
    for i in range(idx,C):
        ans.append(arr[i])
        DFS(cnt+1, i+1)
        ans.pop()
        
DFS(0,0)