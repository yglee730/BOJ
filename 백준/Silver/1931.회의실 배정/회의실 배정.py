N = int(input())

mylist=[]
for i in range(N):
    start, end = map(int, input().split())
    mylist.append([start, end])

mylist = sorted(mylist, key=lambda a: a[0])
mylist = sorted(mylist, key=lambda a: a[1])

cnt = 0
endTime = 0

for i,j in mylist:
    if i >= endTime:
        cnt += 1
        endTime = j

print(cnt)