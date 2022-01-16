import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poke_name = {}
poke_number = {}

for i in range(1, N+1):
    poke_number[i] = input().strip()
    poke_name[poke_number[i]] = i
    
for i in range(M):
    problem = input().strip()
    
    if problem.isdigit():
        print(poke_number[int(problem)])
    elif problem.isalpha():
        print(poke_name[problem])
