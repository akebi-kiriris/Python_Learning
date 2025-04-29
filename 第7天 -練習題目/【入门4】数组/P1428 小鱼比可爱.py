#2025/4/24 12.48-01.00
n = int(input())
arr = list(map(int,input().split()))
check = [0]*n

#第一個已設為0，從第二個往後開始，往前看有幾個比自己小的
for i in range(1,len(arr)):
    temp=0
    while i>temp:
        if arr[i]>arr[temp]:
            check[i]+=1
        temp+=1
        

print(' '.join(map(str,check)))