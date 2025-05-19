n = int(input())

arr=[(i, *input().split()) for i in range(n)]
arr.sort(key=lambda x: (int(x[2]), int(x[3]), int(x[4]), -x[0]))

for i in arr:
    print(i[1])