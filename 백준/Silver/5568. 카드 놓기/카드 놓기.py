from itertools import permutations

n = int(input())
k = int(input())

kard = []
for i in range(n):
    kard.append(input())

res = set()
for i in permutations(kard, k):
    res.add("".join(i))

print(len(res))