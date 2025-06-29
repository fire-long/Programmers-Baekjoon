import sys
T = int(sys.stdin.readline().rstrip())
A = []
for _ in range(T):
    #temp = [map(int, sys.stdin.readline().rstrip().split(' '))].sort(reverse=True)
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    temp.sort(reverse=True)
    A.append(temp[2])
    # .sort(reverse=True)를 변수 선언 시 바로 하면 TypeError: 'NoneType' object is not subscriptable
    # temp가 None으로 인식됨
    # 이유 : .sort 자체가 return None이고, 적용은 선언과 별도로 진행해야 함.

for a in A:
    print(a, end="\n")