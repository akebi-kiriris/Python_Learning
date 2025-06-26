a = int(input())
b = int(input())
m = int(input())
N = int(input())

summ = 0
day = 2
arr = []
arr.append(a)
arr.append(b)
#arr=[a,b]

while arr[-1]<m and day<N:
    day+=1
    arr.append(arr[-1]+arr[-2])
    if arr[-1]>m:
        break

print(sum(arr[:]))