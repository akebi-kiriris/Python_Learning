n = int(input())
fun = ["a","b","c"]
temp = ""

for i in range(n):
    ans = ""
    sen = list(map(str,input().split()))
    
    if temp in fun:
        temp = sen[0]
        
    if sen[0]=="a":
        ans+=sen[1]
        for i in range(2,len(sen)):
            ans+="+"+str(sen[i])
        sen = sum(map(int, sen[1:]))
        ans+="="+str(sen)
        print(f"{ans}")
        print(len(ans))
    elif sen[0]=="b":
        ans+=sen[1]
        for i in range(2,len(sen)):
            ans+="-"+str(sen[i])
        sen = sum(map(int, sen[1:]))
        ans+="="+str(sen)
        print(f"{ans}")
        print(len(ans))
        
# 1
# a 64 46