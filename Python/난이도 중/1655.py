# 백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 
# 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.
# 예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 
# 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오
# N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 
# 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.
import sys
import heapq

count = int(sys.stdin.readline())
valuelist = []

maxheap = [] 
minheap = []

def PushHeap(num, x):
    if num <= maxheap[0] * -1: # 기준 = maxheap[0] * -1, 기준보다 작거나 같으면 max heap으로
        heapq.heappush(maxheap, num * -1)
        if x%2 == 0: # 갯수가 짝수
            if len(maxheap) > len(minheap):
                heapq.heappush(minheap, heapq.heappop(maxheap) * -1)
        if x%2 == 1: # 갯수가 홀수
            pass
            
    else: #기준값보다 클 때 minheap으로
        heapq.heappush(minheap, num)
        if x%2 == 1: # 갯수가 홀수
            if len(maxheap) < len(minheap):
                heapq.heappush(maxheap, heapq.heappop(minheap) * -1)
        if x%2 == 0: # 갯수가 짝수
            pass 
    print(maxheap[0] * -1)
    
for x in range(1,count + 1):
    num = int(sys.stdin.readline())
    if x == 1:
        maxheap.append(num * -1)
        print(num)
    else:
        PushHeap(num, x)
