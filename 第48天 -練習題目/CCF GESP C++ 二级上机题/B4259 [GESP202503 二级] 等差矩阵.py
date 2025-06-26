n,m = map(int,input().split())
temp = 1

for i in range(n):
    for k in range(1,m+1):
        print(temp*k,end=" ")    
    print()
    temp +=1