n= int(input())
arr=list(map(int,input().split()))

arr.sort()
pos = 0
while pos<len(arr)-2:
    if arr[pos]==arr[pos+1]:
        arr.remove(arr[pos])
        pos-=1
    pos+=1
print(len(arr))
print(*arr)