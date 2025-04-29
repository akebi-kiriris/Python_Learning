
l,m = map(int,input().split())

arr = [1]*(l+1)

for i in range(m):
    a,b=map(int,input().split())
    for k in range(a,b+1):
        arr[k]=0

print(sum(arr))
    