arr= []
while True:
    try:
        n=int(input())
        p =int(input())
        k = round(p ** (1 / n))
        while True:
            if k**n==p:
                arr.append(k)
                break
            elif k**n < p:
                k += 1
            else:
                k -= 1
    except:
        break

for i in arr:
    print(i)