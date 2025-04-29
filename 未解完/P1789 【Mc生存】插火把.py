#n*n的範圍，m個火把,k個螢石
n,m,k = map(int,input().split())
torch_pos = []
for i in range(m):
    torch_pos.append(list(map(int, input().split())))

#先產生大小為n*n個，值為0的二維陣列
arr = [[0]*n for i in range(n)]


#先擺火把
for pos in torch_pos:
    x = pos[0]-1
    y = pos[1]-1
    arr[y][x] = 1
    