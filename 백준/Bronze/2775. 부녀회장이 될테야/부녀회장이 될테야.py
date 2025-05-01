import sys
T = int(sys.stdin.readline().rstrip())


for i in range(T):
    k= int(sys.stdin.readline().rstrip()) #floor
    n= int(sys.stdin.readline().rstrip()) #room
    floor0 = [x for x in range(1, n+1)]
    for j in range(k):
        for q in range(1, n):
            floor0[q] += floor0[q-1] 
    print(floor0[-1])
#참고 https://ooyoung.tistory.com/89