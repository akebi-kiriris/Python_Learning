n,m = map(int,input().split())
arr = [[0]*m for i in range(n)]

for i in range(n):
    row = input().strip()
    for k in range(m):
        if k < len(row) and row[k] == '*':
            arr[i][k]="*"

for i in range(n):
        for k in range(m):
            if arr[i][k] == '*': 
                for r in [-1, 0, 1]:
                    for c in [-1, 0, 1]:
                        if r == 0 and c == 0:  
                            continue
                        rp = i+r
                        cp = k+c
                        if 0 <= rp < n and 0 <= cp < m and arr[rp][cp] != '*':
                            arr[rp][cp] += 1
                
for row in arr:
    print(''.join(map(str, row)))
