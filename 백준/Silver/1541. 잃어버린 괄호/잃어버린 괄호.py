calc = input().split('-')

li = []

for val in calc:
    if '+' in val:
        vals = map(int,val.split('+'))
        li.append(sum(vals))
    else:
        li.append(int(val))

ans = li[0]*2

for i in li:
    ans -= i
    
print(ans)