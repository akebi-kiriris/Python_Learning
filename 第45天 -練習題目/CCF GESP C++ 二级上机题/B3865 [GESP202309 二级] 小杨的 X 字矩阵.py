n = int(input())

arr = [["-"]*n for _ in range(n)]
k = 0

#+---+
#-+-+-
for i in range(n//2):
    arr[i][k] = "+"
    arr[i][-1-k] = "+"
    arr[-1-i][k] = "+"
    arr[-1-i][-1-k] = "+"
    k+=1

if n%2!=0:
    arr[n//2][n//2]="+"

for i in arr:
    print(*i,sep="")