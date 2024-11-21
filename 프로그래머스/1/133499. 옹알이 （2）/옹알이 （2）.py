def solution(babbling):
    a = ["aya", "ye", "woo", "ma"]
    count = 0
    c = ""
    for i in babbling:
        while True:
            for x in a:
                if c == x:
                    pass 
                elif i[:len(x)] == x:
                    
                    i = i[len(x):]
                    c = x
                    break  
            else:
                break
        
        if i == "":
            count += 1
        c= ""
    return count