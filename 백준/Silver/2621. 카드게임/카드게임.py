cards = {}
numCount = [0 for _ in range(10)]
number = set()

for _ in range(5):
    color, num = input().split()
    if color in cards:
        cards[color].append(int(num))
    else:
        cards[color] = [int(num)]
    numCount[int(num)] += 1
    number.add(int(num))

def isSameColor(cards):
    if len(cards) == 1:
        return True
    return False

def isContinue(numCount):
    index = 0
    for i in range(1, 10):
        if numCount[i] != 1:
            if numCount[i] != 0:
                return False
        else:
            if index == 0:
                index = i
            else:
                if index + 1 != i:
                    return False
                else:
                    index = i
    return True

def isSameNumber(numCount):
    count = sorted(numCount, reverse=True)
    
    if count[0] == 4:
        return 8
    elif count[0] == 3:
        if count[1] == 2:
            return 7
        else:
            return 4
    elif count[0] == 2:
        if count[1] == 2:
            return 3
        else:
            return 2
        
number = sorted(list(number))
score = 100 + number[-1]

if isSameColor(cards):
    if isContinue(numCount): # case 1
        score = max(score, 900 + number[-1])
    else: # case 4
        score = max(score, 600 + number[-1])
else:
    if isContinue(numCount): # case 5
        score = max(score, 500 + number[-1])

isSameNumber = isSameNumber(numCount)
if isSameNumber == 8: # case 2
    score = max(score, 800 + numCount.index(4))
elif isSameNumber == 7: # case 3
    score = max(score, 700 + numCount.index(3) * 10 + numCount.index(2))
elif isSameNumber == 4: # case 6
    score = max(score, 400 + numCount.index(3))
elif isSameNumber == 3: # case 7
    number1 = numCount.index(2)
    number2 = numCount.index(2, number1+1, 10)
    score = max(score, 300 + number2*10 + number1)
elif isSameNumber == 2: # case 8
    score = max(score, 200 + numCount.index(2))
    
print(score)