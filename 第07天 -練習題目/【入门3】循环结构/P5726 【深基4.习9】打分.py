n = int(input())
arr = list(map(int,input().split()))

arr = sorted(arr)

del arr[0]
del arr[n-2]
print(f"{sum(arr)/(n-2):.2f}")