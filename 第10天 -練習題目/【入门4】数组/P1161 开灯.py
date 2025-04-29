n = int(input())
arr = [0]

for i in range(1,n+1):
    a,t = map(float,input().split())
    if len(arr)<=int(a*t):
        arr += [0] * (int(a*t) - len(arr) + 1)
    for k in range(1,int(t)+1):
        if arr[int(a*k)]==1:
            arr[int(a*k)]=0
        else:
            arr[int(a*k)]=1

print(arr.index(1))