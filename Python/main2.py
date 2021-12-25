import sys
num = int(input())

for x in range(0,num):
    x,y = map(int, sys.stdin.readline().split())
    print(x+y)
    