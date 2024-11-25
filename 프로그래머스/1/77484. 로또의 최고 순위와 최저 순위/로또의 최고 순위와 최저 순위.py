def sum(count):
    if count == 6:
        return 1
    elif count == 5:
        return 2
    elif count == 4:
        return 3
    elif count == 3:
        return 4
    elif count == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    count2 = 0#0의 갯수
    count = 0 #맞춘 갯수
    count3 = len(win_nums)#못맞춘갯수
    c = []
    for i in lottos:
        if i == 0:
            count2+=1

    for x in lottos:
        if x in win_nums:
            count+=1

    c.append(sum(count+count2))

    c.append(sum(count))
    return c