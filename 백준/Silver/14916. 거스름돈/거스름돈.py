import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
# while True:
#     if n%5 == 0:
#         f_cnt += n//5
#         n %= 5
#         if n%2 == 0:
#             t_cnt += n//2
#             n %= 2
#             break
# if t_cnt+f_cnt>=1:
#     print(t_cnt+f_cnt)
# else:
#     print(-1)
#시간초과

#참고 : https://www.acmicpc.net/board/view/101460
if n <= 1 or n==3:
    print(-1)
elif n%5==0:
    cnt = n//5
    print(cnt)
else:
    while n%5 != 0:
        n -= 2
        cnt += 1
    cnt += n//5
    print(cnt)
