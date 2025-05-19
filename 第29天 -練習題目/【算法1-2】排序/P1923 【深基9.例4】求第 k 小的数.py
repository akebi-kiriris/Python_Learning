# import sys
# import array
# input = sys.stdin.readline

# def quick_select(arr,left,right,k):
    
#     if left == right:
#         return arr[left]

#     pivot = arr[(left + right) // 2]
#     l,r = left,right
#     while l<=r:
#         while l <= r and arr[l]<pivot:
#             l+=1
#         while l <= r and arr[r]>pivot:
#             r-=1
            
#         if l <= r:
#             arr[l],arr[r] = arr[r],arr[l]
#             l += 1
#             r -= 1
    

#     if k <= r:
#         return quick_select(arr, left, r, k)
#     elif k >= l:
#         return quick_select(arr, l, right, k)
#     else:
#         return arr[k]
    
# n,k = map(int,input().split())
# arr = array.array('I', map(int, input().split()))
# print(quick_select(arr, 0, n - 1, k))

n,k = map(int,input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)
print(arr[k])

#都一樣會MLE