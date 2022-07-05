import sys

K, L = map(int, input().split())
student = {}

for i in range(L):
    sno = sys.stdin.readline().rstrip()
    if sno in student:
        del student[sno]
    student[sno] = hash(sno)

cnt = 0
for i in student:
    if cnt == K:
        break
    print(i)
    cnt += 1