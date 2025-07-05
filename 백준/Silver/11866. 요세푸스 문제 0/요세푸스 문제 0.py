import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
people = [i for i in range(1, N+1)]
k_index = 0#인덱스. 원형으로 돌아가야하니까!![이 부분 놓쳐서 틀린 것]
result = []
for i in range(N):
    k_index = (k_index+ K-1)%len(people)
    result.append(str(people.pop(k_index))) 
    #str 안 쓰면 print 구문에서 join 사용 못함
print("<",", ".join(result)[:],">", sep='')