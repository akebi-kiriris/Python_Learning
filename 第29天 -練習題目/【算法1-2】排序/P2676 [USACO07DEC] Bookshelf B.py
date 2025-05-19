n,b = map(int,input().split())

arr= [int(input()) for i in range(n)]
arr.sort(reverse=False)

sum = 0
check=0
while sum<=b:
    sum+=arr.pop()
    check+=1
print(check)
