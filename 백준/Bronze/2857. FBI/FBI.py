import sys
stc = []
noFBI = True
for i in range(1, 6, 1):
    s = sys.stdin.readline().rstrip()
    if 'FBI' in s:
        noFBI = False
        print(i, end=" ")
if noFBI:
    print("HE GOT AWAY!")