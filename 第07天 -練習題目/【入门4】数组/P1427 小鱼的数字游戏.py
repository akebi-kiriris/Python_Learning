arr = list(map(int,input().split()))

arr.reverse()
del arr[0]

print(' '.join(map(str,arr)))