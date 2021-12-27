# 백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 
# 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.
# 예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 
# 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오

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
result = [0,0]
if count == 1:
    num = int(sys.stdin.readline())
    print(num)
    

for x in range(1,count + 1):
    num = int(sys.stdin.readline())
    if x == 1:
        result[0] = num
        print(num)
        continue
    elif x == 2:
        result[1] = num
        result = sorted(result)
        print(result[0])
        continue
    else:
        if result[1] >= num:
            if result[0] <= num:
                result[1] = num
        elif result[0] <= num:
            if result[1] >= num:
                result[0] = num
    result = sorted(result)
    print(result[1])
    




