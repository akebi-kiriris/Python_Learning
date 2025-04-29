q = int(input())
sen = list(map(str,input()))
find = ""
out = []
ins = []

for i in range(q):
    req = list(map(str,input().split()))
    if req[0]=="1":
        del req[0]
        out += [''.join(sen + req)]
    elif req[0]=="2":
        st = int(req[1])
        fin = st+int(req[2])
        out+=out[st:fin]
    elif req[0]=="3":
        sen.insert(int(req[1]),req[2])
        out+=sen
    elif req[0]=="4":
        find = req[1]
        del req[0]
        temp = ''.join(map(str,sen))
        out+=str(temp.index(find))

print(out)
print(''.join(map(str,out)))
    
# q = int(input())
# sen = list(map(str,input()))
# find = ""
# out = []

# for i in range(q):
#     req = list(map(str,input().split()))
#     if req[0]=="1":
#         del req[0]
#         sen+=req
#         out+=''.join(map(str,sen))
#     elif req[0]=="2":
#         st = int(req[1])
#         fin = st+int(req[2])
#         sen = sen[st:fin]
#         out+=''.join(map(str,sen))
#     elif req[0]=="3":
#         sen.insert(int(req[1]),req[2])
#         out+=''.join(map(str,sen))
#     elif req[0]=="4":
#         find = req[1]
#         del req[0]
#         temp = ''.join(map(str,sen))
#         out+=temp.index(find)
    
# print(''.join(map(str,out)))