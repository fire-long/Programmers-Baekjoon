import sys
N, M = map(int, sys.stdin.readline().split())
length = []
titles = []
notes = []
for _ in range(N):
    row = list(sys.stdin.readline().rstrip().split())
    length.append(row[0])
    titles.append(row[1])
    notes.append(' '.join(row[2:5]))
jh_notes = []
ans = []
for _ in range(M):
    jh_notes = sys.stdin.readline().rstrip()
    if notes.count(jh_notes) == 1:
        idx = notes.index(jh_notes)
        ans.append(titles[idx])
    elif notes.count(jh_notes) >= 2:
        ans.append('?')
    else:
        ans.append('!')
for x in ans:
    print(x)