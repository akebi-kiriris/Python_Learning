n = int(input())
arr = [["a"]*n for _ in range(n)]

for i in range(n//2+1):
    arr[i][0] = "|"
    arr[i][-1] = "|"
    arr[-i][0] = "|"
    arr[-i][-1] = "|"
       

for i in range(n-2):
    arr[n//2][i+1]="-"

for i in arr:
    print(*i,sep="")