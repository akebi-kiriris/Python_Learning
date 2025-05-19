n,m = map(int,input().split())
arr= [tuple(map(int,input().split())) for i  in range(n)]

arr.sort(key= lambda x:(x[1],-x[0]),reverse=True)
limit = int(m * 1.5)
check = arr[limit - 1][1]

sum = [item for item in arr if item[1] >= check]

print(check,len(sum))
for a,b in sum:
    print(a,b)