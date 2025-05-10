import sys
money = int(sys.stdin.readline().rstrip())
stock_price = list(map(int, sys.stdin.readline().rstrip().split()))

def junhyun(money, stock_price):
    stock = 0 #보유 주식 수
    for i in stock_price:
        stock += money // i #현재가격으로 살 수 있는 최대 수량 매수
        money %= i #남은 현금
    money += stock * stock_price[13] #마지막날에 모든 주식 매도
    return money

def sungmin(money, stock_price):
    stock = 0 #보유 주식 수
    for i in range(len(stock_price) - 4):
        if stock_price[i] > stock_price[i+1] > stock_price[i+2] > stock_price[i+3]:  #3일연속 감소한다면->다음 날 매수
            stock += money // stock_price[i+3]
            money %= stock_price[i+3]
        if stock_price[i] < stock_price[i + 1] < stock_price[i+2] < stock_price[i+3]:  #3인 연속 상승한다면->다음 날 전량 매도
            money += stock_price[i+3] * stock
            stock = 0
    #마지막 날에 보유한 주식 모두 매도
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