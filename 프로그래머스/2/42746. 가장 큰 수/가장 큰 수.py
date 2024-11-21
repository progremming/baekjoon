def solution(lists):
    count = 0
    for i in lists:
        if i == 0:
            count +=1
    if count == len(lists):
        return "0"
    sorted_list = marge(lists)

    result = ''.join(map(str, sorted_list))
    return result

def marge(lists):
    if len(lists) <= 1:
        return lists
    mids = len(lists) // 2

    l = lists[:mids]
    r = lists[mids:]

    le = marge(l)
    ri = marge(r)

    return sum(le, ri)

def sum(l, r):
    c = []
    while l and r:
        if str(l[0]) + str(r[0]) > str(r[0]) + str(l[0]):
            c.append(l[0])
            l.pop(0)
        else:
            c.append(r[0])
            r.pop(0)
    c.extend(l)
    c.extend(r)
    return c  