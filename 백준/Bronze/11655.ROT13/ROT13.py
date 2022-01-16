word = input()
rot = []

for i in range(len(word)):
    op = ord(word[i])
    
    if 65 <= op & op <= 90:
        op2 = op + 13
        
        if op2 > 90:
            rot.append(65 + (op2%91))
        else:
            rot.append(op2)
    elif 97 <= op & op <= 122:
        op2 = op + 13
        
        if op2 > 122:
            rot.append(97 + (op2%123))
        else:
            rot.append(op2)
    else:
        rot.append(op)
        
           
for i in range(len(rot)):
    print(chr(rot[i]), end='')