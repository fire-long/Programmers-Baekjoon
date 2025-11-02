def solution(sizes):
    max_x = 0
    max_y = 0
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if sizes[i][0] > max_x:
            max_x = sizes[i][0]    
        if sizes[i][1] > max_y:
            max_y = sizes[i][1]
    return max_x * max_y