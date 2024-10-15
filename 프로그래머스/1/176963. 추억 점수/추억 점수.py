def solution(name, yearning, photo):
    c = 0
    d = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for x in photo:
        for t in x:
            if t not in dic:
                pass
            else:
                c = c + dic.get(t)
        d.append(c)
        c = 0
    
    
    return d