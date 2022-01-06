import sys
input = sys.stdin.readline

def CalcBC(N,K):
    dp = [[0] * (K+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(min(i,K) + 1):
            if (j == 0 or j == i):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i -1][j]
    return dp[N][K]

N,K = map(int, input().split())
print(CalcBC(N,K))