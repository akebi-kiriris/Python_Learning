bx,by,hx,hy = map(int,input().split())

#馬的移動
horse_pos = [ (0, 0),
    (1, 2), (2, 1), (-1, 2), (-2, 1),
    (1, -2), (2, -1), (-1, -2), (-2, -1)
]
#棋盤
dp = [[0] * (by + 1) for _ in range(bx + 1)]


#看馬控制那些地方
for a,b in horse_pos:
    if a+hx>bx+1 or a+hx<0 or b+hy>by+1 or b+hy<0:
        continue
    dp[a+hx][b+hy] = -1

#馬沒佔領起始點就把它設為1
if dp[0][0]!=-1:
    dp[0][0]=1

for i in range(0,bx+1):
    for j in range(0,by+1):
        #如果要算的位置被馬佔領就跳過
        if dp[i][j] == -1:
            continue
        #防止出界，並防止算入被馬佔領的地方，不可能從被馬佔領的那格過來
        if i>0 and dp[i - 1][j] != -1:
            dp[i][j]+=dp[i-1][j]
        if j>0 and dp[i][j - 1] != -1:
            dp[i][j]+=dp[i][j-1]

print(dp[bx][by])


    
           