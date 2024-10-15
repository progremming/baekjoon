def solution(s):
    stack = []  
    cnt = 0
    l_cnt = 0
    r_cnt = 0
    i = 0
    while i < len(s):
        stack.append(s[i])
        if len(stack) == 1:
            pass
        if stack[0] != stack[-1]:
            cnt = cnt + 1
            r_cnt = r_cnt + 1
        if stack[0] == stack[-1]:
            cnt = cnt - 1
            l_cnt = l_cnt + 1
        if l_cnt < r_cnt:
            return False
        i = i + 1
    if cnt == 0 and stack[0] == "(":
        if l_cnt == r_cnt:
            return True
        else:
            return False
    else:
        return False