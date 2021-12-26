# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

num = int(input())
for x in range(1, num+1):
    stars = ''
    for z in range(1, x+1):
        stars += '*'
    print(stars)
