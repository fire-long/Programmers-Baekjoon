import sys

# command = sys.stdin.readline().rstrip().split() #여기에 list붙이면 이중 리스트됨
# for i in range(1, len(command)):
#     strings = command[i][::-1].replace(';', '').replace(',','').replace('][', '[]')
#     print(command[0]+strings[:-1], strings[-1]+';')
#변수명까지 바뀌어버림 -> 수정 필요
base, *rest = sys.stdin.readline().rstrip().replace(';', '').split()
for token in rest:
    var = ''
    symbol = ''
    for c in reversed(token.replace(',','')):
        if c.isalpha():
            var = c + var
        else:
            symbol += c
    symbol = symbol.replace('][', '[]')
    print(f"{base}{symbol} {var};")

#*rest는 나머지 요소를 리스트로 받는다는 unpacking 문법


#아래는 다른 분 코드 참고
# for i in command:
#     flag=0
#     if (i==command[0]):
#         continue
#     i=i[:-1]#,와 ; 등 문자 제거
#     for j in range(len(i)):
#         if (i[j].isalpha()==1): #알파벳인지 숫자인지 여부 확인
#             #->변수명 시작 인덱스인 j
#             for k in range(j+1, len(i)):
#                 #k는 기호가 시작되는 위치
#                 flag=1
#                 break
#     if (flag==1):
#         #변수명 뒤에 있으면
#         tmp=i[k:][::-1]+" "+i[j:k]+';'
#     else:
#         tmp=" "+i[j:]+';'
#     tmp=tmp.replace('][', '[]')
#     print(command[0]+tmp)

