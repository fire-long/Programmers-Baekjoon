import sys
n = int(sys.stdin.readline().rstrip())
p = [0, 1]
for i in range(2, n+1):
    #p[i] = p[i-1] + p[i-2] #IndexError: list assignment index out of range
    p.append(p[i-1]+p[i-2])
print(p[n])