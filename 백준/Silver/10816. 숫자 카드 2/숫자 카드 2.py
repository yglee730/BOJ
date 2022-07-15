import sys

N = int(sys.stdin.readline().rstrip())
NList = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
MList = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in NList:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in MList:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')