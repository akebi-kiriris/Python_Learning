k = int(input())
n = 0
check = 1
while n<=k:
    n += 1/check
    check+=1

print(check-1)