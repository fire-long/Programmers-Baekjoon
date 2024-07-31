import sys
word = sys.stdin.readline().strip()
reversed_word = [r for r in word[::-1]]
palindrome = 1
for i in range(len(word)):
    if word[i] != reversed_word[i]:
        palindrome = 0
print(palindrome)