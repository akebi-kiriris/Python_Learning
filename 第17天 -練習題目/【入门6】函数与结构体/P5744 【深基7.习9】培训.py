n = int(input())

arr = [list(map(str,input().split())) for i in range(n)]

for i in range(n):
    arr[i][1] = int(arr[i][1])+1
    arr[i][2]=600 if int(arr[i][2])*1.2>600 else int(int(arr[i][2])*1.2)


for i in arr:
    print(' '.join(map(str,i)))
    