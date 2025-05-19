n = int(input())
hs = 0
pos = 0

arr=[list(map(str,input().split())) for i in range(n)]

for i in range(len(arr)):
    scores = list(map(int, arr[i][1:]))
    current_sum = sum(scores)  
    if current_sum>hs:
        hs = current_sum
        pos = i
        
print(' '.join(arr[pos])) 