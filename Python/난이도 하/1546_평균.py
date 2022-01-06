

import sys
input = sys.stdin.readline

def CalcAverage(N, Nums):
    avarage = 0
    sum = 0
    maxnum = max(Nums)

    for i in Nums:
        sum += i / maxnum * 100
    avarage = sum / N
    
    return avarage    

N = float(input())


avarage = CalcAverage(N,Nums)
print(avarage)