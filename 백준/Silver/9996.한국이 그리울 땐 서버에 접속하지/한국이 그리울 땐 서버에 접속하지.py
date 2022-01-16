num = int(input())
pattern = input().split('*')

start = pattern[0]
end = pattern[1]

fileName = []
for i in range(num):
    fileName = input()
    
    if ((fileName[:len(start)]) == start) & ((fileName[-len(end):]) == end) & (len("".join(pattern)) <= len(fileName)):
        print('DA')
    else:
        print('NE')
