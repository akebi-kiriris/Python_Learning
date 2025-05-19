n = int(input())
arr=[]
while len(arr) < n:
    arr += list(map(int, input().split()))
check = 0
for i in range(n):
    for k in range(n-i-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1] = arr[k+1],arr[k]
            check+=1
print(check)