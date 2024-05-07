import sys
input_list = [0 for _ in range(30)]

for i in range(28):
    N = int(sys.stdin.readline())
    input_list[N-1] = 1

absence = [i for i, x in enumerate(input_list) if x==0]
print(absence[0]+1)
print(absence[1]+1)