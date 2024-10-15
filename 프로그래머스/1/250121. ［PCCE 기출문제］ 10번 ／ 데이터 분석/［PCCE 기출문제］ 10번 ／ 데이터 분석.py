def solution(data, ext, val_ext, sort_by):
    dic = {
        "date": 1,
        "code": 0,
        "maximum": 2,
        "remain": 3
    }

    exte = dic[ext]
    sort_idx = dic[sort_by]
    filtered_data = []
    for x in data:
        if x[exte] < val_ext:  
            filtered_data.append(x)  
    for i in range(len(filtered_data)):
        for j in range(i + 1, len(filtered_data)):
            if filtered_data[i][sort_idx] > filtered_data[j][sort_idx]:
                filtered_data[i], filtered_data[j] = filtered_data[j], filtered_data[i]

    return filtered_data