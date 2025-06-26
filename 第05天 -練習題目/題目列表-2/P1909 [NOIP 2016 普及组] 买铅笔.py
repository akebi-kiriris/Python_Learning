from math import ceil
n = int(input())
arr = []
sum = [[0, 0] for _ in range(3)]  # deepseek解

for i in range(3):
    a,b = map(int,input().split())
    arr.append([a,b])
    
for i in range(3):
    sum[i][0] = ceil(n/arr[i][0])  #算數量
    sum[i][1] = sum[i][0]*arr[i][1] #算價格

min_cost = min(sum[0][1], sum[1][1], sum[2][1])

print(min_cost)


#deepseek解
# import math

# n = int(input())
# min_cost = float('inf')

# for _ in range(3):
#     a, b = map(int, input().split())
#     packages = math.ceil(n / a)
#     total_cost = packages * b
#     if total_cost < min_cost:
#         min_cost = total_cost

# print(min_cost)
