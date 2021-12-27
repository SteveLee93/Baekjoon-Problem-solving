# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

#key point = result[i][j] = max(value + result[i - 1][j - weight], result[i - 1][j])

N,K = map(int,input().split())
WV = [[0,0]]
result = [[0] * (K+1) for i in range(N+1)]

for i in range(N):
    WV.append(list(map(int, input().split())))


for i in range(1, N+1):
    for j in range(1,K+1):
        weight = WV[i][0]
        value = WV[i][1]
        
        if j < weight:
            result[i][j] = result[i - 1][j]
        else:
            result[i][j] = max(value + result[i - 1][j - weight], result[i - 1][j])

print(result[N][K])