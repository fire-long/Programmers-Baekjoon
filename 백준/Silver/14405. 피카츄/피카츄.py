import sys
S = sys.stdin.readline().rstrip()
#replace 쓰면 간단해짐
S = S.replace('pi',' ')
S = S.replace('ka',' ')
S = S.replace('chu',' ')
if len(S.strip())!=0:
    print("NO")
else:
    print("YES")