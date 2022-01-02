# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 이진 탐색

import sys
input = sys.stdin.readline



N_Num = int(input())
N_list = list(map(int, input().split()))


M_Num = int(input())
M_list = list(map(int, input().split()))

for i in range(0,M_Num):
    if N_list.count(M_list[i]) > 0:
        print(1)
    else:
        print(0)

