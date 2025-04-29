# n = int(input())
# arr = list(map(int,input().split()))
# check = 0

# #外圈該數字，內圈該數字依序往後，兩數字相加檢查是否在arr裡
# for i in range(n):
#     for k in range(i+1,n):
#         if (arr[i]+arr[k]) in arr:
#             check+=1

# print(check)

n = int(input())
arr = list(map(int,input().split()))
check = [0]*n

#外圈該數字，內圈該數字依序往後，兩數字相加檢查是否在arr裡。
#改為放進陣列
for i in range(n):
    for k in range(i+1,n):
        if (arr[i]+arr[k]) in arr:
            check[arr.index(arr[i]+arr[k])]=1

print(sum(check))