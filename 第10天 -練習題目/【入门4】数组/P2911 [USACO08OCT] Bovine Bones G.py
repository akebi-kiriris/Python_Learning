d1,d2,d3 = map(int,input().split())

d1r = [i for i in range(1, d1 + 1)]
d2r = [i for i in range(1, d2 + 1)]
d3r = [i for i in range(1, d3 + 1)]

arr = [0]*(d1+d2+d3+1)

for i in d1r:
    for k in d2r:
        for m in d3r:
            arr[i+k+m] +=1

print(arr.index(max(arr)))