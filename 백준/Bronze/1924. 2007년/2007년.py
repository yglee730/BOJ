x, y = map(int, input().split())

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

res = 0

for i in range(x):
    res += day[i]
    
print(week[(res+y)%7])