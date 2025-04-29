digits = {
    '0': ["XXX", "X.X", "X.X", "X.X", "XXX"],
    '1': ["..X", "..X", "..X", "..X", "..X"],
    '2': ["XXX", "..X", "XXX", "X..", "XXX"],
    '3': ["XXX", "..X", "XXX", "..X", "XXX"],
    '4': ["X.X", "X.X", "XXX", "..X", "..X"],
    '5': ["XXX", "X..", "XXX", "..X", "XXX"],
    '6': ["XXX", "X..", "XXX", "X.X", "XXX"],
    '7': ["XXX", "..X", "..X", "..X", "..X"],
    '8': ["XXX", "X.X", "XXX", "X.X", "XXX"],
    '9': ["XXX", "X.X", "XXX", "..X", "XXX"]
}

d = int(input())  
n = input() 

#5行輸出
output = [''] * 5  

#看到哪個數字，將該數字加入每一行
for i in range(d):
    num = n[i]
    digit = digits[num]  
    
    for row in range(5):
        if output[row]!='':
            output[row] +="."+digit[row]
        else:
            output[row] = digit[row]


for i in output:
    print(i)
    
    # for row in range(5):
    #     if output[row]:
    #         output[row] +="."+digit[row]
    #     else:
    #         output[row] = digit[row]