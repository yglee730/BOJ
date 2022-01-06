word = input()
alpha = [0 for i in range(26)]

for i in range(len(word)):
    alpha[ord(word[i])%97] += 1
    
for i in range(len(alpha)):
    print(alpha[i], end= ' ')