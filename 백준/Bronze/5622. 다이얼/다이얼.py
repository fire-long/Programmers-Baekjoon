import sys
S = sys.stdin.readline().strip()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
T=0
for s in S:
    for idx, d in enumerate(dial):
        if s in d:
            T += (idx+3)
            break
print(T)