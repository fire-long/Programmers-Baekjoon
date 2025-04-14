import sys
N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0

for number in numbers:
    count = 0
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                count+=1
        if count == 0:
            result +=1

print(result)
#https://c1.cheerthaipower.com/paisseon-sosu-panbyeol-while/
#https://zks145.tistory.com/32