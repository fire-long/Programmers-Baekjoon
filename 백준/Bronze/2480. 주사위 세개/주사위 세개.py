N,M,L = map(int, input().split())
prize = 0
if N==M==L:
    prize = 10000+N*1000
elif (N==M):
    prize = 1000 + N*100
elif (M==L):
    prize = 1000 + M*100
elif (L==N):
    prize = 1000 + L*100
else:
    if (N>=M)&(N>=L):
        prize = N*100
    elif (M>=N)&(M>=L):
        prize = M*100
    elif (L>=M)&(L>=N):
        prize = L*100
print(prize)