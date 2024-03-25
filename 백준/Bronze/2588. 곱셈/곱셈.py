N = input()
M = input()
third = int(N)*int(M[2])
fourth = int(N)*int(M[1])
fifth = int(N)*int(M[0])
sixth = third + fourth * 10 + fifth * 100
print(f"{third}\n{fourth}\n{fifth}\n{sixth}")