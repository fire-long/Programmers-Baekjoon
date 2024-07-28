import sys
white_numbers = list(map(int, sys.stdin.readline().split()))
standard_numbers = [1, 1, 2, 2, 2, 8]

for i in range(len(white_numbers)):
    print(standard_numbers[i]-white_numbers[i], end=' ')