n = input()
pos = [0]*26
for i in n:
    pos[ord(i)-ord('a')] += 1

pos = [i for i in pos if i>0]
check = max(pos)-min(pos)

        
if check <2:
    print("No Answer",0,sep='\n')
else:
    for i in range(2,int(check**0.5)+1):
        if check%i==0:
            print("No Answer",0,sep='\n')
            break
            
    else:
        print("Lucky Word",check,sep='\n')