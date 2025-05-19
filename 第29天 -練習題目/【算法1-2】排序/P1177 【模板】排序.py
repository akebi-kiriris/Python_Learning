
#氣泡演算法，TLE，沒料
# for k in range(n):
#     for i in range(n-k-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]

#Quick sort
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    
    left = [x for x in arr if x<pivot]
    mid = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]
    return quick_sort(left)+mid+quick_sort(right)
n = int(input())
arr = list(map(int,input().split()))
print(*quick_sort(arr))