word = input()
alpha = [0 for i in range(26)]

odd = 0
answer = ""
tmp = ""

for i in word:
    alpha[ord(i)-65] += 1
    
for i in range(len(alpha)):
    if alpha[i] % 2 == 1:
        odd += 1
        tmp = chr(i+65)
    answer += chr(i+65) * (alpha[i]//2)

reverse_answer = list(answer)
reverse_answer.reverse()

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer+tmp+"".join(map(str, reverse_answer)))