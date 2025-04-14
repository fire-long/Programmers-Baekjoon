import sys
D, H, W = map(int, sys.stdin.readline().rstrip().split())

d = (H**2+W**2)**0.5
ratio = D/d
print(int(H*ratio), int(W*ratio))