k = int(input())
list = []

for i in range(k):
    n = int(input())
    
    if n != 0:
        list.append(n)
    else:
        list.pop(-1)
        
print(sum(list))