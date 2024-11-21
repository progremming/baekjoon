def solution(babbling):
    a = ["aya", "ye", "woo", "ma"]
    count = 0

    for i in babbling:
        while True:
            for x in a:
                if i[:len(x)] == x:
                    i = i[len(x):]
                    break  
            else:
                break
        
        if i == "":
            count += 1

    return count
