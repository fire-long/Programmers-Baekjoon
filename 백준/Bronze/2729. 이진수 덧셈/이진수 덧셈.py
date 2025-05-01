import sys
T = int(sys.stdin.readline().rstrip())
sums=[]
for t in range(0, T):
    n1, n2 = sys.stdin.readline().rstrip().split()
    sums.append(bin(int(n1,2)+int(n2,2))[2:])
#print(bin(s, 2) for s in sums) #<generator object <genexpr> at ~
#generator 객체 그대로 출력해버리는데 이는 print 구문 내에 표현식을 넣어서임
print("\n".join(sums))
#참고 : https://kyull-it.tistory.com/120