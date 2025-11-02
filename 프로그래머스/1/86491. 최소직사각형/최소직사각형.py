def solution(sizes):
    max_x = 0
    max_y = 0
    for s in sizes:
        if s[0] > s[1]:
            s[0], s[1] = s[1], s[0]
        if s[0] > max_x:
            max_x = s[0]    
        if s[1] > max_y:
            max_y = s[1]
    return max_x * max_y