# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys

num = int(input())
result = []
max = 0
for x in range(0,num):
    result.append(int(sys.stdin.readline()))

for x in sorted(result):
    print(x)
    

