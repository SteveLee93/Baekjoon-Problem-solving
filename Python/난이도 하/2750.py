# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

num = int(input())
result = []
for x in range(0,num):
    result.append(int(input()))

for x in sorted(result):
    print(x)