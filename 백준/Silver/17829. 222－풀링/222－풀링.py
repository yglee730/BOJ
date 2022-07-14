import sys

N = int(sys.stdin.readline())
CNN = []

CNN = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

while len(CNN) != 1:
    new = []
    for i in range(0, len(CNN), 2):
        tmp = []
        for j in range(0, len(CNN), 2):
            calc = sorted([CNN[i][j], CNN[i+1][j], CNN[i][j+1], CNN[i+1][j+1]], reverse = True)
            tmp.append(calc[1])
        new.append(tmp)
    CNN = new
    # print(CNN)
    # print("==================================")
print(CNN[0][0])