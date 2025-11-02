def solution(arr):
    idx = arr.index(min(arr))
    arr.pop(idx)
    answer = arr if arr != [] else [-1]
    return answer