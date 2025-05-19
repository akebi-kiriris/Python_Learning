n = int(input())
arr = []
for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)

for i in range(n):
    if (arr[i][1])+(arr[i][2])>140 and (arr[i][1])*7+(arr[i][2])*3>=800:
        print("Excellent")
    else:
        print("Not excellent")