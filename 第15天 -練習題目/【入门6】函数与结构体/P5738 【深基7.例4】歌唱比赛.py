def cal(singer):
    singer.remove(min(singer))
    singer.remove(max(singer))
    return sum(singer)/len(singer)



n,m = map(int,input().split())
arr = []
temp = 0
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in arr:
    current = cal(i)  
    temp = current if temp < current else temp

print(f"{temp:.2f}")