A, B, C = map(int, input().split())

def calc(B):
    if B == 1:
        return A % C
    else:
        op = calc(B//2)
        if (B%2) == 0:
            return (op * op) % C
        else:
            return (op * op * A) % C            
    
print(calc(B))