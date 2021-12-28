# 백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 
# 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.
# 예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 
# 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오
# N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 
# 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.
import sys

# #O(n) 
# result = []
# count = int(sys.stdin.readline())

# for x in range(1,count+1):
#     num = int(sys.stdin.readline())
#     result.append(num)
#     result = sorted(result)
#     if x%2 == 0:            # 짝수개
#         print(result[int(x/2) - 1])
#     else:                   # 홀수개
#         print(result[int(x/2)])

count = int(sys.stdin.readline())
result = []
mid = 0
maxcount = 0
mincount = 0

for x in range(1,count + 1):
    num = int(sys.stdin.readline())
    if x == 1:
        result.append(num)
        print(num)

    elif x == 2:
        if result[0] <= num:
            result.append(num)
        else:
            result.insert(0, num) 
        print(min(result))

    elif x == 3:
        if num < result[0]:
            result.insert(0, num)
        elif num >= result[0] and num < result[1]:
            result.insert(1,num)
        else:
            result.append(num)
        print(result[1])

    elif x % 2 == 1: # 홀수 개
        midindex = int(x/2) 
        if num <= result[midindex - 1]:
            result.insert(midindex - 1, num)
        elif num > result[midindex - 1] and num <= result[midindex + 1]:
            result.insert(midindex, num)
        else:
            result.insert(midindex + 1, num)
        print(result[midindex])

    elif x % 2 == 0: # 짝수 개
        midindex = int(x/2) 
        if num <= result[midindex - 2]:
            result.insert(midindex - 2, num)
        elif num > result[midindex - 2] and num <= result[midindex - 1]:
            result.insert(midindex - 1, num)
        elif num > result[midindex - 1] and num <= result[midindex]:
            result.insert(midindex, num)
        else:
            result.insert(midindex + 1, num)
        print(result[midindex -1])
