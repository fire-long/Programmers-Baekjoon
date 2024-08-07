import sys

word = sys.stdin.readline().strip()

'''
if "c=" in word:
    word = word.replace('c=', 'č')
if "c-" in word:
    word = word.replace('c-', 'ć')
if "dz=" in word:
    word = word.replace('dz=', 'dž')
if "d-" in word:
    word = word.replace('d-', 'đ')
if "lj" in word:
    word = word.replace('lj', 'lj')
if "nj" in word:
    word = word.replace('nj', 'nj')
if "s=" in word:
    word = word.replace('s=', 'š')
if "z=" in word:
    word = word.replace('z=', 'ž')
'''
i = 0
count = 0
while i<len(word):
    chars = word[i:i+2]
    if chars in ["c=","c-","d-","lj","nj","s=","z="]:
        count += 1
        i += 2
    elif i+2<len(word) and word[i:i+3] == "dz=":
        count += 1
        i += 3
    else:
        count += 1
        i += 1

print(count)