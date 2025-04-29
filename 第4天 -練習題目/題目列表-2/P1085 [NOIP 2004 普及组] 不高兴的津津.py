max = 0
for i in range(7):
    f,s = map(int,input().split())
    if i ==0:
        max = f+s
        check = i+1
    if f+s>max:
        check = i+1
        max = f+s
if max>8:
    print(check)
else:
    print(0)








#arr.append([y, m])

