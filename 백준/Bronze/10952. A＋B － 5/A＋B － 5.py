import sys
answers=[]
while(1):
    A,B = map(int, sys.stdin.readline().split())
    answers.append(A+B)
    if A==0 and B==0:
         break;
answers.remove(0)
for i in answers:
    print(i)