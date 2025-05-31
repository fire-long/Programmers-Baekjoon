import sys
a = int(sys.stdin.readline().rstrip()) #진행 사람 수
t = int(sys.stdin.readline().rstrip()) #t번째
s = int(sys.stdin.readline().rstrip()) #뻔=0, 데기=1

bun = 0 #뻔 개수
degi = 0 #데기 개수
cnt = 0 #회차
n = []
while True:
    cnt += 1

    for _ in range(2):
        bun += 1
        n.append((bun, 0)) #튜플 추가
        degi += 1
        n.append((degi, 1))
    for _ in range(cnt+1):
        bun += 1
        n.append((bun, 0))
    for _ in range(cnt+1):
        degi += 1
        n.append((degi, 1))
    
    if bun>=t:
        print(n.index((t, s))%a) #t번째로 등장한 s 종류의 인덱스를 찾아서 
        #사람 수로 나눈 나머지가 즉 그 인덱스에 위치한 사람 번호
        break