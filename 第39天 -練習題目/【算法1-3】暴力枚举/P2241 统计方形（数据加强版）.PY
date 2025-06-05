n,m = map(int,input().split())

#將左下角視為形狀的起始點，並調整x、y重複尋找該形狀，
#正方形為當前x、y的最小值，長方形為總矩形數-正方形數，總矩形數為當前x*y
# square = 0
# total = 0

# for x in range(1,n+1):
#     for y in range(1,m+1):
#         square+=min(x,y)
#         total += x*y
    
# print(square,total-square)  


#上解可用，但會tle，只能套公式。
min_side = min(n, m)
squares = min_side * (min_side + 1) * (2 * min_side + 1) // 6
squares += (max(n, m) - min_side) * min_side * (min_side + 1) // 2


total = n * (n + 1) // 2 * m * (m + 1) // 2


print(squares, total - squares)