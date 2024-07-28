import sys
white_numbers = list(map(int, sys.stdin.readline().split()))
standard_numbers = [1, 1, 2, 2, 2, 8]

for s, w in zip(standard_numbers, white_numbers):
    print(s-w, end=' ')