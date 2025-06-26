n = int(input())
check_each = 0
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    for k in range(i+1,n):
        if abs(arr[i][0] -arr[k][0])<=5 and abs(arr[i][1] -arr[k][1])<=5 and abs(arr[i][2] -arr[k][2])<=5 :
            if abs(sum(arr[i])-sum(arr[k]))<=10:
                check_each +=1

print(check_each)
            
            
        