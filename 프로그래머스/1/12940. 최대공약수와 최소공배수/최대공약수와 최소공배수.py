def solution(a, b):
    c = []
    d = []
    e = []
    f = []

    for i in range(1,a+1):
    
        if (a % i == 0):
            c.append(i)

    for i in range(1,b+1):
        
        if (b % i == 0):
            d.append(i)



    for i in range(len(c)):
        for x in range(len(d)):
            if c[i] == d[x]:
                e.append(c[i])

    f.append(max(e))
    f.append(a*b/max(e))

    return f