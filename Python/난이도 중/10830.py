# 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)
# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다. 
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다. 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.
import sys
input = sys.stdin.readline

def CalcMatrixPow(A,Y):
    result = GetUnitMatrix(A)
    temp = A
    while(Y > 0):
        if Y % 2 == 1:
            result = CalcMatrixMulti(result, temp)
        temp = CalcMatrixMulti(temp, temp)
        Y = int(Y/2)
    return result

def CalcMatrixMulti(A, B):
    result = [[0] * (len(A)) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                result[i][k] += A[i][j] * B[j][k]
    
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] %= 1000
    return result

def GetUnitMatrix(A):
    result = [[0] * (len(A)) for _ in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == j: result[i][j] = 1
    return result

N,B = map(int,input().split())

values = []
for i in range(N):
    rowvalues = list(map(int,input().split()))
    values.append(rowvalues)

result = CalcMatrixPow(values,B)

for x in range(N):
    print(*result[x], sep = ' ', end = '\n')





