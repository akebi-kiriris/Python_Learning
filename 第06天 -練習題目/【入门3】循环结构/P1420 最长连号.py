n = int(input())
arr = list(map(int,input().split()))
temp = 1  #當前連續
max = 1   #最大連續

for i in range(0,len(arr)-1):
    if arr[i+1]==arr[i]+1:
        temp+=1
    elif arr[i+1]!=arr[i]+1:
        if max<temp:
            max = temp
        temp=1
        
# 補最後一組也可能是最長的情況
if max < temp:
    max = temp
print(max)
        