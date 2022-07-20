N = int(input())

cnt = 0
money = 1000 - N
exist = [500,100,50,10,5,1]

for i in exist:
    tmp = money//i
    
    cnt += (tmp)
    money %= i

print(cnt)