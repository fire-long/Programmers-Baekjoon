import sys
stc = []
while True:
    
    stc.append(sys.stdin.readline().strip().lower())
    
    if stc[-1]=='#':
        stc.remove('#')
        for s in stc:
            cnt = 0
            for c in s:
                if c in ['a', 'e', 'i', 'o', 'u']:
                    cnt += 1
            print(cnt)
        break