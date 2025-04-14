import sys
res = []
for _ in range(3):
    res.append(sys.stdin.readline().rstrip().count('0'))

for i in range(3):
    if res[i] == 1: print("A")
    elif res[i] == 2: print("B")
    elif res[i] == 3: print("C")
    elif res[i] == 4: print("D")
    elif res[i] == 0:print("E")