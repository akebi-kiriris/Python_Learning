ISBN = input()

check = (int(ISBN[0])*1+int(ISBN[2])*2+int(ISBN[3])*3+int(ISBN[4])*4+int(ISBN[6])*5+int(ISBN[7])*6+int(ISBN[8])*7+int(ISBN[9])*8+int(ISBN[10])*9)%11

check_char ='X' if check==10 else str(check)

if check_char == ISBN[12]:
    print("Right")
else:
    print(ISBN[:12] + check_char)
    
    
#deepseek
# ISBN = input().replace('-', '')
# check = (int(ISBN[0]) + int(ISBN[1]) * 2 + int(ISBN[2]) * 3 + int(ISBN[3]) * 4 +
#          int(ISBN[4]) * 5 + int(ISBN[5]) * 6 + int(ISBN[6]) * 7 + int(ISBN[7]) * 8 +
#          int(ISBN[8]) * 9) % 11