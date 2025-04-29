n = int(input())
arr = [[0] * (i+1) for i in range(n)]


curr_row = 0 #當前行數
pos = 0      #填到哪裡

#先填第一行
arr[0][0]=1
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 填之後那幾行，一個一個填
for i in range(1,n):
    pos =0
    while pos <= i:  
        if pos == 0 or pos == i:
            arr[i][pos] = 1
        else:
            #填前一排位置相同的和前一排的前一個
            arr[i][pos] = arr[i-1][pos-1] + arr[i-1][pos]
        pos += 1


for row in arr:
    print(' '.join(f'{int(x):d}' for x in row))