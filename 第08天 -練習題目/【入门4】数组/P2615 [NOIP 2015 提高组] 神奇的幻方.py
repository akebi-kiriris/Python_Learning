n = int(input())

arr=[[''] * n for _ in range(n)]

x = n // 2 
y = 0
arr[y][x] = 1

for i in range(2, n * n + 1):
    if y==0 and x!=n-1:
        x +=1
        y=n-1
        arr[y][x] =i
    elif y!=0 and x==n-1:
        x = 0
        y = y-1
        arr[y][x] = i
    elif y==0 and x==n-1:
        x = n-1
        y+=1
        arr[y][x] = i
    elif y!=0 and x!=n-1:
        if arr[y-1][x+1]=='':
            y-=1
            x+=1
            arr[y][x] = i
        else:
            y +=1
            arr[y][x] = i

for row in arr:
    check=0
    print(' '.join(map(str, row)))
    check+=1
    if check==n-1:
        print('')
    


