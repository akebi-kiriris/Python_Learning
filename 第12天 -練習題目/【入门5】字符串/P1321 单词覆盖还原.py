arr = list(input())
lent = len(arr)
boy_check=0
girl_check=0
for i in range(2):
    arr.append(".")

#當第一個為b，則+1並結束，當第一為o，只要前一個不是b就可
for i in range(lent):
    if arr[i]=="b":
        boy_check+=1
    elif arr[i]=="o" and arr[i-1]!="b":
        boy_check+=1
    elif arr[i]=="y" and arr[i-1]!="o":
        boy_check+=1
    elif arr[i]=="g":
        girl_check+=1
    elif arr[i]=="i" and arr[i-1]!="g":
        girl_check+=1
    elif arr[i]=="r" and arr[i-1]!="i":
        girl_check+=1
    elif arr[i]=="l" and arr[i-1]!="r":
        girl_check+=1
        
print(boy_check,girl_check,sep="\n")
#1 1 1 1