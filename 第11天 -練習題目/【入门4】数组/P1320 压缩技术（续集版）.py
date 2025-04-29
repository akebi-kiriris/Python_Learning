arr = []
check =0
show_list = []

while True:
    line = input()
    n = len(line)
    arr += [int(c) for c in line]
    check+=1
    if n == check:
        break

show_list.append(n)

check = 0
temp = 0
for i in arr:
    if i==check:
        temp+=1
        continue
    check=1-check
    show_list.append(temp)
    temp=1
show_list.append(temp)

print(' '.join(map(str,show_list)))