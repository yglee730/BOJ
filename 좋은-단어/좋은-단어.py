n = int(input())
cnt = 0

for i in range(n):
    word = input().rstrip()
    stack = []
    
    for j in range(len(word)):
        if stack:
            if stack[-1] == word[j]:
                stack.pop()
            else:
                stack.append(word[j])
        else:
            stack.append(word[j])

    if not stack:
        cnt += 1

print(cnt)