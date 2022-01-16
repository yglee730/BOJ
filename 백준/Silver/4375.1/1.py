while True:
    try:
        inputNum = int(input())
    except EOFError:
        break
    
    if inputNum == 0:
        print(1)
        continue
    
    number = 1
    
    while True:
        if (number%inputNum) == 0:
            print(len(str(number)))
            break
        else:    
            number = number*10+1