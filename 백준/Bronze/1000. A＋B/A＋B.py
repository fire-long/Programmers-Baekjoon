import sys

a,b=input().split()
#input()으로는 소요시간이 오래 걸려서 sys.stdin.readline()으로 변경하곤 하는데
#이거 보니까 sys 쓰면 소요시간이 더 길어짐
print(int(a)+int(b))