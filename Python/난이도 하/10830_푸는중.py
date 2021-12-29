# 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)
# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다. 
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다. 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.
import sys
input = sys.stdin.readline

def CalcPow(X,Y):
    result = 1
    thirdresult = X
    while(Y > 0):
        if Y%2 == 1:
            result *= thirdresult
            result %= 1000
        thirdresult = ((thirdresult%1000) * (thirdresult%1000)) % 1000
        Y = int(Y/2)
    return result

N,B = map(int,input().split())

values = []
for i in range(N):
    rowvalues = list(map(int,input().split()))
    for j in range(len(rowvalues)):
        rowvalues[j] = CalcPow(rowvalues[j], B)
    values.append(rowvalues)

for x in range(N):
    print(*values[x], sep = ' ', end = '\n')





