import sys
org_word = sys.stdin.readline().strip().upper()

#전체 알파벳 리스트
word_list = [0]*26

for i in range(ord('A'), ord('Z')+1):
    if chr(i) in org_word:
        word_list[i-65] = org_word.count(chr(i))


if word_list.count(max(word_list)) >=2:
    print("?")
else:
    print(chr(word_list.index(max(word_list))+ord('A')))