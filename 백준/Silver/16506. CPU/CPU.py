import sys
N = int(sys.stdin.readline().rstrip())
result=[]
for _ in range(N):
    opcode,*rest = sys.stdin.readline().rstrip().split()
    rD, rA, rB_C = int(rest[0]), int(rest[1]), int(rest[2])
    #레지스터 번호와 즉시값의 길이를 정확하게 맞춰야 함.
    if 'ADD' in opcode:
        r = '0000'
        if 'ADD' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    elif 'SUB' in opcode:
        r = '0001'
        if 'SUB' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    elif 'MOV' in opcode:
        r = '0010'
        rA = '000'
        if 'MOV' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    elif 'AND' in opcode:
        r = '0011'
        if 'AND' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    elif 'OR' in opcode:
        r = '0100'
        if 'OR' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    elif 'NOT' in opcode:
        r = '01010'
        rA = '000'
        rB_C = bin(rB_C)[2:]
        rB = rB_C.zfill(3)
        rB = rB+'0'
    elif 'MULT' in opcode:
        r = '0110'
        if 'MULT' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    elif 'LSFTL' in opcode:
        r = '0111'
        if 'LSFTL' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    elif 'LSFTR' in opcode:
        r = '1000'
        if 'LSFTR' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    elif 'ASFTR' in opcode:
        r = '1001'
        if 'ASFTR' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    elif 'RL' in opcode:
        r = '1010'
        if 'RL' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    elif 'RR' in opcode:
        r = '1011'
        if 'RR' == opcode:
            r+='0'
            rB_C = bin(rB_C)[2:]
            rB = rB_C.zfill(3)
            rB = rB+'0'
        else:
            r+='1'
            rB = bin(rB_C)[2:]
            rB = rB.zfill(4)
    rD = bin(rD)[2:]
    rD = rD.zfill(3)
    r +='0'+rD
    
    
    if rA == '000':
        r+= rA+rB
    else:
        rA = bin(rA)[2:]
        rA = rA.zfill(3)
        r+= rA+rB


    result.append(r)

print('\n'.join(result))

#참고:https://kkamikoon.tistory.com/entry/Python-%EC%8A%A4%ED%8A%B8%EB%A7%81-%EC%95%9E%EC%97%90-0-%EC%B1%84%EC%9A%B0%EB%8A%94-%EB%B0%A9%EB%B2%95zfill-rjust