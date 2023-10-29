#백트래킹 문제

N = int(input())
arr = []
def backtracking(idx):
    for i in range(1, (idx//2) + 1):
        if arr[-i:] == arr[-2 * i : -i]:
            return -1
    if idx == N:
        for n in arr:
            print(n, end = "")
        print()
        return 0
    for i in range(1, 4):
        arr.append(i)
        if backtracking(idx + 1) == 0:
            return 0
        arr.pop()
backtracking(0)