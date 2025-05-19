n = int(input())
arr = list(map(int,input().split())) 

for k in range(n):  
    for i in range(n-1):
        now = arr[i]
        next_num = arr[i+1]  
        
        if int(str(now) + str(next_num)) < int(str(next_num) + str(now)):
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(''.join(map(str,arr)))

#deepseek解
# n = int(input())
# arr = list(map(str, input().split()))  # 保持字符串形式便于拼接

# # 自定义排序：比较a+b和b+a的大小
# arr.sort(key=lambda x: x, reverse=True)  # 先按字典序排
# arr.sort(key=lambda x: x*10, reverse=True)  # 关键：通过字符串乘法比较拼接结果

# print(''.join(arr))