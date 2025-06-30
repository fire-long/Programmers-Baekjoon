import sys
N = int(sys.stdin.readline().rstrip())
cnt = 0

for i in range(N):
    text = sys.stdin.readline().rstrip()
    is_group = True

    for t in range(len(text)):
        prev = text[:t] 
        if t>0:
            if text[t] != text[t-1] and text[t] in prev:
                #TypeError: unsupported operand type(s) for &: 'str' and 'str'
                #조건식에서는 비트 AND 연산자 대신 and으로 바꿔 사용해서 해결
                # continue
                is_group = False
                break
            # else:
            #     cnt += 1
            #여기서 바로 else문을 쓰면 4로 처리됨.
    if is_group:
        cnt += 1
        
print(cnt)