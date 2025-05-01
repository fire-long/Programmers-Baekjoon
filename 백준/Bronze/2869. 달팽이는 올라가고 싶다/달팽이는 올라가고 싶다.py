import sys
A, B, V = map(int, sys.stdin.readline().rstrip().split())
# day = 0
##시간초과
# while V > 0:
#     day += 1
#     #상승
#     V -= A
#     if V<=0 :
#         break
#     #하강
#     V += B
#print(day)

day=(V-B)/(A-B)
print(int(day) if day == int(day) else int(day)+1)
#참고
#https://stultus.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-2869-%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94-%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0-%EC%8B%B6%EB%8B%A4