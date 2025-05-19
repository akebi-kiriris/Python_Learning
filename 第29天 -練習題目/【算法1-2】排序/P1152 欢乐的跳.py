arr = list(map(int,input().split()))
out = []
for i in range(1,len(arr)-1):
    out.append(abs(arr[i]-arr[i+1]))
out.sort()
for i in range(arr[0]-1):
    if out[i]!=i+1:
        print("Not jolly")
        break
else:
    print("Jolly")