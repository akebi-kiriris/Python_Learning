#2025/4/24 01.05 - 01.16
n = int(input())
check = n
arr = []
arr.append(n)
while check!=1:
    if check%2==0:
        check/=2
        arr.append(check)
    else:
        check = check*3+1
        arr.append(check)

arr.reverse()
arr = map(int,arr)

print(' '.join(map(str,arr)))