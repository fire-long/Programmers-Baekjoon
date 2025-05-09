import sys
money = int(sys.stdin.readline().rstrip())
stock_price = list(map(int, sys.stdin.readline().rstrip().split()))

def junhyun(money, stock_price):
    stock = 0
    for i in stock_price:
        stock += money // i
        money %= i
    money += stock * stock_price[13]
    return money

def sungmin(money, stock_price):
    stock = 0
    for i in range(len(stock_price) - 4):
        if stock_price[i] > stock_price[i+1] > stock_price[i+2] > stock_price[i+3]:  # 3일연속 감소한다면
            stock += money // stock_price[i+3]
            money %= stock_price[i+3]
        if stock_price[i] < stock_price[i + 1] < stock_price[i+2] < stock_price[i+3]:  # 3인 연속 상승한다면
            money += stock_price[i+3] * stock
            stock = 0
    money += stock_price[-1] * stock
    return money


m_j = junhyun(money, stock_price)
m_s = sungmin(money, stock_price)

if (m_j > m_s):
    print("BNP")
elif m_j < m_s:
    print("TIMING")
else:
    print("SAMESAME")