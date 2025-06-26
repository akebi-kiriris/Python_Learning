arr = list(map(int,input().split()))
abc = input()
ans=[0]*3 
#找最大最小
for i in range(3):
    if abc[i]=='A':
        t_a = i
    elif abc[i]=='C':
        t_c = i


t_b = 3-t_a-t_c
arr = sorted(arr)
ans[t_a] = arr[0]
ans[t_b] = arr[1]
ans[t_c] = arr[2]


print(' '.join(map(str, ans)))
    
    
#先找最大最小在哪，得知ABC位置 ，取先取最大值擺C，再取最小值擺A
#宣告空陣列 ans=[0]*3
#print(' '.join(map(str, ans))) 只能join字串