import sys
N = int(sys.stdin.readline().rstrip())
actual_ingredients = list(sys.stdin.readline().rstrip().split())
hj_ingredients = list(sys.stdin.readline().rstrip().split())

print((set(actual_ingredients) - set(hj_ingredients)).pop())