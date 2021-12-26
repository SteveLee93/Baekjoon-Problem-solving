# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력의 마지막에는 0 두 개가 들어온다.

while(True):
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break
    print(x+y)