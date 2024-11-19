def solution(number, k):
    del_count = 0
    stack = []  

    for digit in number:
        while stack and del_count < k and stack[-1] < digit:
            stack.pop()
            del_count += 1
        stack.append(digit)


    while del_count < k:
        stack.pop()
        del_count += 1

    return ''.join(stack)
