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

