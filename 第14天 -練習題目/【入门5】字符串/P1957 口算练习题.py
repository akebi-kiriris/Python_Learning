n = int(input())
fun = ["a","b","c"]
temp = ""
check = 0
arr = [[0, 0] for i in range(n)]
for i in range(n):
    ans = ""
    sen = input().split()
    temp  = sen[0] if sen[0] in fun else temp
    check = 1 if sen[0] in fun else 0
        
    if temp=="a":
        temp = "a"
        ans+=sen[check]
        for j in range(check+1,len(sen)):
            ans+="+"+str(sen[j])
        sen = sum(map(int, sen[check:]))
        ans+="="+str(sen)
    elif temp=="b":
        temp = "b"
        ans+=sen[check]
        for j in range(check+1,len(sen)):
            ans+="-"+str(sen[j])
        sen = int(sen[check])-int(sen[check+1])
        ans+="="+str(sen)
    elif temp=="c":
        temp="c"
        ans+=sen[check]
        for j in range(check+1,len(sen)):
            ans+="*"+str(sen[j])
        sen = int(sen[check])*int(sen[check+1])
        ans+="="+str(sen)
    arr[i][0] = f"{ans}"
    arr[i][1] = len(ans)
       
for i in range(n):
    print(arr[i][0]) 
    print(arr[i][1]) 

# 1
# b 46 64