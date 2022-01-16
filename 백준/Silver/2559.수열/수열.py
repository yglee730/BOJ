N, K = map(int, input().split())
Tmp = list(map(int, input().split()))

TmpSum = sum(Tmp[:K])
Tmp_result = [TmpSum]

for i in range(len(Tmp)-K):
    TmpSum = TmpSum - Tmp[i] + Tmp[i+K]
    Tmp_result.append(TmpSum)

print(max(Tmp_result))