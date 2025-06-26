s = float(input())
dis = 0
step = 0
temp = 2
while dis<s:
    dis += temp
    temp *=0.98
    step+=1

print(step) 