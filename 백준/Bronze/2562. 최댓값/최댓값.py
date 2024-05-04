import sys
input_list = []
for i in range(9):
    input_list.append(int(sys.stdin.readline()))
    
print(max(input_list))
print(input_list.index(max(input_list))+1)#인덱스 + 1