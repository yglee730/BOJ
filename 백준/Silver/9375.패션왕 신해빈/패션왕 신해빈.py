import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    enter = int(input())
    kind = {}
    div_result = 0
    
    for j in range(enter):
        cloth = input().split()
        
        if cloth[1] in kind:
            kind[cloth[1]] = int(kind[cloth[1]])+1
        else:
            kind[cloth[1]] = 1
    
    div_result = 1
    for key, value in kind.items():
        div_result = div_result * (int(kind[key])+1)
            
    print(div_result-1)