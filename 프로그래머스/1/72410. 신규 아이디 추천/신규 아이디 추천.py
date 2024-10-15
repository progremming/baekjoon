def solution(new_id):
    c = []
    
    for i in new_id:
        if i.isalnum() or i in ['-', '_', '.']:
            if len(c) == 0:
                c.append(i.lower() if i.isalpha() else i)
            elif i == '.' and c[-1] == '.':
                continue
            else:
                c.append(i.lower() if i.isalpha() else i)

    if c and c[0] == ".":
        c.pop(0)  
    if c and c[-1] == ".":
        c.pop()  

    if len(c) == 0:
        c.append("a")

    while len(c) < 3:
        c.append(c[-1])

    if len(c) > 15:  # 16자 초과 시 처리
        c = c[:15]
        if c[-1] == ".":
            c.pop()

    return ''.join(c)