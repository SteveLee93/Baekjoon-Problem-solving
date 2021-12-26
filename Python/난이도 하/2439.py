# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

num = int(input())
for x in range(1, num+1):
    stars = ''

    for y in reversed(range(x, num)): 
        stars += ' '

    for z in range(1, x+1):
        stars += '*'
    print(stars)
