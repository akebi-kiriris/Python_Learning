n = int(input())

arr = [[0] * n for k in range(n)]
check =n-1 #該轉了
p = 0    #動了幾步
temp =0  #每兩次轉降一次要求
temp_x=1 #x移動方向
temp_y=0 #y移動方向

#先填第一行
for i in range(n):
    arr[0][i] = i + 1

    
x=n-1
y=0
temp_x = 0 
temp_y = 1

    
#從左到右，到底往下，到下往左，到上往右...
#n=3 ->3 2 2 1 f  n=4 ->4 3 3 2 2 1 f
for i in range(n+1, n*n+1):
    # 移動
    x += temp_x
    y += temp_y
    arr[y][x] = i
    p += 1
    
    #該轉了
    if p==check:
        p=0
        temp+=1
        #轉向
        if temp == 2:
            check -= 1  
            temp=0
            
        if temp_x == 1 and temp_y == 0: #若是向右，改為向下
            temp_x=0
            temp_y=1
        elif temp_x == 0 and temp_y == 1:#若是向下，改為向左
            temp_x=-1
            temp_y=0
        elif temp_x == -1 and temp_y == 0:#若是向左，改為向上
            temp_x=0
            temp_y=-1
        elif temp_x == 0 and temp_y == -1:#若是向上，改為向右
            temp_x=1
            temp_y=0 


for row in arr:
    print(''.join(f'{x:3d}' for x in row))
