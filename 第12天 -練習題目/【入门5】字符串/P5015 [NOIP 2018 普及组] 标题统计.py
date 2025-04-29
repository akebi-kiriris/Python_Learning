# n = list(input())

# for i in n:
#     if i==" "or i=="\n":
#         del n[n.index(i)]

# print(len(n))

n = list(input())
check =0

for i in n:
    if i!=" " and i!="\n":
        check+=1

print(check)  