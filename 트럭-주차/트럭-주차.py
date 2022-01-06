A, B, C = map(int, input().split())
truck = [list(map(int, input().split())) for _ in range(3)]

time = [0 for i in range(101)]

for parking in truck:
    for t in range(parking[0], parking[1]):
        time[t] += 1

price = 0

for i in range(len(time)):
    #print(time[i], end=' ')
    if time[i] == 1:
        price += time[i]*A
        
    if time[i] == 2:
        price += time[i]*B
        
    if time[i] == 3:
        price += time[i]*C
        
print(price)