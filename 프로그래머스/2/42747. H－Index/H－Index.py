def solution(lists):

    lists.sort(reverse=True)
    

    for i in range(len(lists)):
        if lists[i] < i + 1:
            return i
    

    return len(lists)
print(solution([1,2,3,4,5]))