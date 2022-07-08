import sys

N, M = map(int, input().split())

site = {}

for i in range(N):
    name, pwd = sys.stdin.readline().rstrip().split()
    site[name] = pwd

findPwd = []

for i in range(M):
    find = sys.stdin.readline().rstrip()
    findPwd.append(find)

ans = []

for siteName in findPwd:
    ans.append(site[siteName])

for pwd in ans:
    print(pwd)