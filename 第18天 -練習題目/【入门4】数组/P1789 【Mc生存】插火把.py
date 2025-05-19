#n*n的範圍，m個火把,k個螢石
n,m,k = map(int,input().split())
#先產生大小為n*n，值為0的二維陣列
arr = [[0]*n for i in range(n)]

#插火把
for i in range(m):
    x,y = map(int,input().split())
    x-=1
    y-=1
    for px in range(-2,3):
        for py in range(-2,3):
            #先算出該格是否包含在火把照亮的範圍內(上下左右2格範圍、四個角落(1+1=2))
            if abs(px) + abs(py) <= 2:
                nx, ny = x + px, y + py
                #檢查是否在arr範圍內，若在內則將其改為1
                if 0 <= nx < n and 0 <= ny < n:  
                    arr[ny][nx] = 1  

for i in range(k):
    x,y = map(int,input().split())
    x-=1
    y-=1
    for px in range(-2,3):
        for py in range(-2,3):
            nx, ny = x + px, y + py
            #檢查是否在arr範圍內，若在內則將其改為1
            if 0 <= nx < n and 0 <= ny < n:  
                arr[ny][nx] = 1

sum = 0
for i in arr:
    sum +=i.count(0)
print(sum)
#一開始都先遍歷5*5的範圍，火把多限制在曼哈頓距離內。並檢查座標是否超出方陣範圍。