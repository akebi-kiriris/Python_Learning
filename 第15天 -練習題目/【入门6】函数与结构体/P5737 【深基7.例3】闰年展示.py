def is_r(year):
    if year%4==0 and year%100!=0:
        return year
    elif year%100==0 and year%400==0:
        return year
    else: 
        return 0



x,y = map(int,input().split())
arr = []
for i in range(x,y+1):
    if is_r(i)!=0:
        arr.append(i)

print(len(arr))
print(" ".join(map(str,arr)))
