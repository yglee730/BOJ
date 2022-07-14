def recursion(st, start, lenSt):
    tmp = lenSt//3

    if tmp==0:
        return

    for i in range(start+tmp, start+tmp*2):
        st[i] = ' '

    recursion(st, start, tmp)
    recursion(st, start+tmp*2, tmp)

while True:
    try:
        n=int(input())
        if n=='':
            break
        st = ['-' for _ in range(3**n)]
        recursion(st, 0, 3**n)
        ans = ''.join(st)
        print(ans)
    except EOFError:
            break