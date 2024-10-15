def solution(s, skip, index):
    import string


    lists = list(string.ascii_lowercase)
    z = []


    new_list = [] 

    for char in lists:  
        if char not in skip:  
            new_list.append(char)  

   
    for char in s:
        if char in new_list:  

            
            current_index = new_list.index(char) 
          
            new_index = (current_index + index) % len(new_list)

            z.append(new_list[new_index])  
        else:
            z.append(char)  

    return ''.join(z)  
