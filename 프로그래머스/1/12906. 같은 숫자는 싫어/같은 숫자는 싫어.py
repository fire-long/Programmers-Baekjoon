def solution(arr):
    uniques = []
    for i in range(0, len(arr)):
        if arr[i] not in uniques:
            uniques.append(arr[i])
        elif arr[i] != arr[i-1]:
            uniques.append(arr[i])
    answer = uniques
    return answer