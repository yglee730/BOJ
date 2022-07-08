from itertools import permutations

S = input()
res = set()

for i in range(len(S)):
    for j in range(i,len(S)):
        st = S[i:j+1]
        res.add(st)
            
print(len(res))