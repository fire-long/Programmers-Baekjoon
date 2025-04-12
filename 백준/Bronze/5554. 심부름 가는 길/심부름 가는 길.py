import sys
fhts = int(sys.stdin.readline().strip())
fstp = int(sys.stdin.readline().strip())
fpth = int(sys.stdin.readline().strip())
fhth = int(sys.stdin.readline().strip())

total_sec = fhts+fstp+fpth+fhth

print(total_sec//60)
print(total_sec%60)