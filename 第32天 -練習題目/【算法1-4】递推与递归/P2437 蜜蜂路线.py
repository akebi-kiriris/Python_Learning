m, n = map(int, input().split())
k = n - m
dp = [0] * (k + 2)  
dp[0] = 1
dp[1] = 1

for i in range(2, k + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[k])