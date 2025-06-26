x = int(input())

if x/2==x//2:
    check_1 = 1
else:
    check_1 = 0

if x>4 and x<=12:
    check_2 = 1
else:
    check_2 = 0


print(check_1,end=' ')
print(check_1 or check_2,end=' ')
print(check_1^check_2,end=' ')
print(int(not(check_1 or check_2)),end=' ')
    

      