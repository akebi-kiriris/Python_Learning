n = int(input())
arr=[]
for i in range(n):
    check = int(input())
    if check%10>=5:
        arr.append(check+10-check%10)
    else:
        arr.append(check-check%10)
print(*arr,sep="\n")