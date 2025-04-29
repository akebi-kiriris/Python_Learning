arr = list(map(int,input().split()))
n = arr[0]
del arr[0]
show_list = [0] *n**2

now = 0
check = 0

for i in arr:
    for k in range(now,now+i):
        show_list[k] = check
    now = now+i
    check = 1 - check   #deepseek

now = 0
for i in range(1,n+1):
    # print(*show_list[now:n*i]) #*list(展開陣列)
    print(''.join(map(str,show_list[now:n*i])))
    now = n*i