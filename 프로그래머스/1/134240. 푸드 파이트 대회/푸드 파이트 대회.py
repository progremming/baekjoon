def solution(food):
    head = []
    footer = []

    index = 0

    for i in food:
        if i <= 1:
            index +=1
            pass
        elif i % 2 == 1:
            i  = i - 1
            for z in range(i//2):
                head.append(index) 
                footer.append(index)
            index += 1
        else:
            for z in range(i//2):
                head.append(index) 
                footer.append(index)
            index += 1

    head.append(0)
    c = reversed(footer)
    for i in c:
        head.append(i)

    result = ''.join(map(str, head))


    return result