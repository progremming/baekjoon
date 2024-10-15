def solution(answers):

    patterns = [
        [1, 2, 3, 4, 5],  
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  
    ]
    

    scores = [0, 0, 0]

    for i in range(len(answers)):
        for j in range(len(patterns)):

            if answers[i] == patterns[j][i % len(patterns[j])]:
                scores[j] += 1 

    max_score = max(scores)
    result = [i + 1 for i in range(len(scores)) if scores[i] == max_score]
    
    return result


print(solution([1, 3, 2, 4, 2]))  
