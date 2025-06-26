n = int(input())

arr = [["-"]*n for _ in range(n)]

for i in range(n):
    arr[i][0]="+"
    arr[i][-1]="+"

for i in range(n):
    arr[i][i]="+"

for i in arr:
    print(*i,sep="")