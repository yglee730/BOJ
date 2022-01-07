num = int(input())
name = []
alpha = [0 for i in range(26)]

for i in range(num):
    name.append(input())

for i in range(len(name)):
    code = ord(name[i][0]) % 97
    alpha[code] += 1

result = []

for i in range(len(alpha)):    
    if alpha[i] >= 5:
        result.append(chr(i+97))


if len(result) != 0:
    for i in range(len(result)):
        print(result[i], end='')
else:
    print('PREDAJA')