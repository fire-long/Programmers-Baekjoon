import sys, math
D, H, W = map(int,sys.stdin.readline().rstrip().split())

d = math.sqrt(H**2+W**2)
ratio = D/d
print(int(H*ratio), int(W*ratio))