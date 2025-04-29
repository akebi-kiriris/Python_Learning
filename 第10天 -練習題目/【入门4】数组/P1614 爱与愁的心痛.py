n,m = map(int,input().split())
arr = [int(input()) for i in range(n)]
pos = 0
mini = 100000000000000000000

for i in range(n-m+1):
    if mini>sum(arr[i:i+m]):
        mini=sum(arr[i:i+m])


print(mini)