def solution(code):
    mode = 0
    let = []
    
    for i in range(len(code)):
        if mode == 0:
            if code[i] == "1":
                mode = 1
            else:
                if i % 2 == 0:
                    let.append(code[i])         

        elif mode == 1:
            if code[i] != "1":
                if i % 2 == 1:
                    let.append(code[i])
            else:
                mode = 0

    let = ''.join(map(str,let))
    if len(let) == 0:
        return "EMPTY"
    return let
