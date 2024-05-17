import sys
#sys는 개행문자 포함해서 읽어오는 경우가 있기때문에, strip()을 써주는 게 좋음
N = int(sys.stdin.readline().strip())
num = sys.stdin.readline().strip()
li = [int(n) for n in num]
print(sum(li))