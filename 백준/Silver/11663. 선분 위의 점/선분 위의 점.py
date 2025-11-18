import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
coords = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(M):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0
    
    #start보다 크고 end보다 작은 지점을 찾기 위해선
    #이진 탐색을 사용해야 함!
    
    #left, right: 배열 인덱스 범위 좁히는 용도
    # mid:현재 비교 대상으로 삼는 배열 인덱스
    left = 0
    right = N-1
    
    #mid값을 계속 업데이트해서 범위 지정  
    #lower_bound과 upper_bound는 인덱스
    lower_bound = N #start 이상인 값이 없을 수 있음
    upper_bound = -1 #end 이하인 값이 없을 수 있음
    
    while left <= right:
        mid = (left+right)//2
        
        if coords[mid] < start:
            left = mid + 1
            
        elif coords[mid] >= start:
            lower_bound = mid #조건을 만족하는 인덱스 저장
            right = mid - 1
    
    left = 0
    right = N-1
    
    while left <= right:
        mid = (left+right)//2
        
        if coords[mid] > end:
            right = mid - 1
               
        elif coords[mid] <= end:
            upper_bound = mid #조건을 만족하는 인덱스 저장
            left = mid + 1
    
    count = max(0, upper_bound - lower_bound + 1)
    print(count)