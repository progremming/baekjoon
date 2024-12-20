def solution(a,b):
    stack = []
    count = 0
    for i in b:
        c = i - 1
        for x in range(len(a)):
            if a[x][c] > 0:
                stack.append(a[x][c])
                a[x][c] = 0
                if len(stack) == 1 or len(stack) == 0:
                    pass
                elif stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    count = count + 2
                break
    return count