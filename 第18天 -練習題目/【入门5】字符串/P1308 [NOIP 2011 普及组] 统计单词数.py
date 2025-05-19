word = input().lower()
ori = input().lower()
sen = ori.split()
check = [0,-1]

m_text = ' ' + ori + ' '
m_word = ' ' + word +' '

check[0] = sen.count(word)

first_pos = m_text.find(m_word)
if first_pos != -1:
    check[1] = first_pos  
    
check[0] = sen.count(word)
        
if check[0]==0:
    print(-1)
else:  
    print(' '.join(map(str,check)))


