q = int(input())
sen = list(input().strip())
find = ""
out = []

for i in range(q):
    req = input().strip().split()
    if req[0]=="1":
        s = req[1]
        sen.extend(list(s))
        out.append(''.join(sen))
    elif req[0]=="2":
        st = int(req[1])
        fin = st+int(req[2])
        sen = sen[st:fin]
        out.append(''.join(sen))
    elif req[0]=="3":
        a = int(req[1])
        s = req[2]
        sen[a:a] = list(s) 
        out.append(''.join(sen))
    elif req[0]=="4":
        find = req[1]
        temp = ''.join(sen)
        idx = temp.find(find)
        out.append(str(idx))

for i in out:
    print(i)
    
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