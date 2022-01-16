N = int(input())
arrN = list(map(int, input().split()))
arrN.sort()

M = int(input())
arrM = list(map(int, input().split()))

def binary(arrM):
    right = N - 1 
    left = 0
    
    while left <= right:
        mid = (right + left) // 2
        
        if arrN[mid] == arrM:
            return True
    
        if arrM < arrN[mid]:
            right = mid - 1
        elif arrM > arrN[mid]:
            left = mid + 1
        
for i in range(M):
    if binary(arrM[i]):
        print(1)
    else:
        print(0)