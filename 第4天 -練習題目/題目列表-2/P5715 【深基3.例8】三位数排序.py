arr = list(map(int, input().split()))

if arr[0]>arr[1]:
    temp = arr[1]
    arr[1] = arr[0]
    arr[0] = temp
if arr[1]>arr[2]:
    temp = arr[2]
    arr[2] = arr[1]
    arr[1] = temp
if arr[0]>arr[1]:
    temp = arr[1]
    arr[1] = arr[0]
    arr[0] = temp
    
print(' '.join(map(str, arr)))    
# 3 2 1
# 2 3 1
# 1 2 3
# 1 3 2

#deepseek
# arr = list(map(int, input().split()))
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]  # 交換
# if arr[1] > arr[2]:
#     arr[1], arr[2] = arr[2], arr[1]
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]

#網路上
# a,b,c = list(map(int, input().split()))
# if a>b:
#     a,b = b,a
# if a>c:
#     a,c = c,a
# if b>c:
#     b,c = c,b
# print(a,b,c,end=' ')
