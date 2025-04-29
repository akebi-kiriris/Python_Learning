#長 寬 高
w,x,h = map(int,input().split())
q = int(input())

arr = [[[1 for i in range(w)] for j in range(x)] for k in range(h)]
#arr[高][長][寬]
#arr[h][x][w]
#arr[z][y][x]
cube =[]

#分組輸入
for i in range(q):
    cube.append(list(map(int,input().split())))

#分組將對應位置改為0
for i in range(q):
    #x y z長度
    x = cube[i][3]-cube[i][0]+1
    y = cube[i][4]-cube[i][1]+1
    z = cube[i][5]-cube[i][2]+1
    sx = cube[i][0]
    sy = cube[i][1]
    sz = cube[i][2]
    for k in range(sz, sz + z):
        for j in range(sy, sy + y):
            for m in range(sx, sx + x):
                arr[k][j][m] = 0
        

ans = 0
for layer in arr:
    for row in layer:
        for cell in row:
            if cell == 1:
                ans += 1
print(ans)