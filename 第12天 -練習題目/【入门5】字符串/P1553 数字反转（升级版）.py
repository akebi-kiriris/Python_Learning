s = list(input())
s.reverse()

#先判斷是否為百分比(狀況四)
if s[0]=="%":
    del s[0]
    if len(s)!=1:              #可能為01200%
        while s and s[0]=="0":
            del s[0]
    if len(s)==0:
        s.append("0")
    s.append("%")
    print(''.join(s))
#在判斷是否為分數(狀況三)
elif "/" in s:
    s.reverse()
    pos = s.index("/")
    fro = s[0:pos] 
    beh = s[pos+1:]
    fro.reverse()  
    if len(fro)!=1:
        while fro and fro[0]=="0":
            del fro[0]
    beh.reverse() 
    while beh[0]=="0":
        del beh[0]
    if len(fro) == 0:
        fro.append("0")
    print(''.join(fro)+"/"+''.join(beh))
#判斷是否為小數(狀況二) 小改狀況三
elif "." in s:
    s.reverse()
    pos = s.index(".")
    fro = s[0:pos] 
    beh = s[pos+1:]
    fro.reverse()
    if len(fro)!=1:  
        while fro and fro[0]=="0":
            del fro[0]
    beh.reverse()
    while beh and beh[-1]=="0":
        del beh[-1]
    if len(beh) == 0:
        beh.append("0") 
    if len(fro) == 0:
        fro.append("0")
    print(''.join(fro)+"."+''.join(beh))
    
#判斷是否為整數
else:
    if len(s)==1 and "0" in s:
        print(0)
    
    else:
        while s[0]=="0":
            del s[0]
        print(''.join(s))