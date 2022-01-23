N = int(input())

def process(N, start, target, sup):
    if N == 1:
        print(start, target)
    else:
        process(N-1, start, sup, target)
        print(start, target)
        process(N-1, sup, target, start)

print(2**N-1)    
process(N, 1, 3, 2)