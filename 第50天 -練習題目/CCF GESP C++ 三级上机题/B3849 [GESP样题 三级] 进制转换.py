n = int(input())
r = int(input())
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
out = []

#假設25進位
#625(25*25) 25
#不斷除以*進位的* 
#餘數為該位數字
#123 25 
#23 4
#4 N
while n > 0:
    remainder = n % r
    out.append(digits[remainder])
    n //= r
#因為進位轉換是從最低位開始的，所以要反過來印
out.reverse()
print("".join(out))
