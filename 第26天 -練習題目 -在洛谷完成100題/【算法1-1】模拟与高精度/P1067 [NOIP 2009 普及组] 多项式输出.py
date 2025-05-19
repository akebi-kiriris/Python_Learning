# n = int(input())
# arr=list(map(int,input().split()))
# out =[]
# first = True
# for i in range(n):
#     coeff = arr[i]
#     power = n-i
#     if n-i==1:
#         out.append(f"{arr[i]:-}x")
#     elif arr[i]!=0 and abs(arr[i])!=1:
#         out.append(f"{arr[i]:-}x^{n-i}")
#     elif arr[i]==1:
#         out.append(f"+x^{n-i}")
#     elif arr[i]==-1:
#         out.append(f"-x^{n-i}")
# out.append(f"{arr[-1]:+}")
# print(''.join(map(str,out)))

#1.先判斷是否為第一(去正或帶負)，若非第一則帶正或帶負。
#2.再來判斷係數，若係數為1或0則不顯示係數，只顯示正負。
#3.再來判斷次方，若次方為1或0也不顯示


n = int(input())
arr=list(map(int,input().split()))
out =[]
first = True

for i in range(n+1):
    coeff = arr[i]
    power = n-i
    sign = ""
    term = ""  
    
    #係數為0則過
    if coeff ==0:
        continue
    
    #判斷是否為首項，附上正負
    if not first:
        sign = "+" if arr[i]>0 else "-"
    elif coeff<0:
        sign = "-"
    first = False

    abs_coeff = abs(coeff)
    
    #判斷次方是否為1或0和判斷係數是否為1
    if power==0:
        term = f"{abs_coeff}"
    elif power==1:
        if abs_coeff==1:
            term = f"x"
        else:
            term = f"{abs_coeff}x"
    else:
        if abs_coeff==1:
            term = f"x^{power}"
        else:
            term = f"{abs_coeff}x^{power}"
    out.append(sign + term)
print(''.join(out))