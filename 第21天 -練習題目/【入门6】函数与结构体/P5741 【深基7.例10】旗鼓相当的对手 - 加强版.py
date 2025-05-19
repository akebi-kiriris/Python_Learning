n = int(input())
arr = []
out = []
for i in range(n):
    arr.append(list(map(str,input().split())))

for now in range(n):
    for next in range(now+1,n):
        if (abs(sum(map(int, arr[now][1:])) -sum(map(int, arr[next][1:]))) <=10 and
              abs(int(arr[now][1])-int(arr[next][1]))<=5 and
              abs(int(arr[now][2])-int(arr[next][2]))<=5 and
              abs(int(arr[now][3])-int(arr[next][3]))<=5 ):
            if arr[now][0]>arr[next][0]:
                out.append((arr[next][0],arr[now][0]))
            elif arr[now][0]<arr[next][0]:
                out.append((arr[now][0],arr[next][0]))

out.sort()

for i in out:
    print(i[0],i[1])