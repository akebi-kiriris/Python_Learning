n = int(input())

dp=[0]*(n+1)
dp[0]=1

for i in range(1,n+1):
    dp[i]=int(dp[i-1]*2*(2*i-1)/(i+1))
print(dp[n])
