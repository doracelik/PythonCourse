# Dora Celik 64324 HW1
#Adding cash, withdrawing cash and showing portfolio/account history works according to my testings with the instructions. However, I couldn't manage to implement the rest.

import random

class stock(object):
    def __init__(self, price, ticker):
        self.price = price
        self.ticker = ticker
        self.stocksinport = 0

class MutualFund(object):
    def __init__(self, price, fund_name):
        self.fund_name = fund_name
        self.price = price
        self.fundsinport = 0


class Portfolio():
    def __init__(self):
        self.cash = 0
        self.stock = []
        self.mutualfund = []
        self.hist = ["\nAccount Summary:"] #Defines to summarize the portfolio

    def addCash(self, amount):
        self.cash += amount
        self.hist.append(f"${amount} added to your account.") #Adding cash, I tried to use string formatting (like %d, %s) but it gave me error. Then I asked a friend of mine)

    def withdrawCash(self, amount):
        self.cash -= amount
        if self.cash < 0:
            print ("You have insufficient funds in your account")
        else:
            self.hist.append(f"You withdrew ${amount} from your account.") #Withdrawing cash. Same as above, I tried to use string formatting but it didn't work.

    def buyStock(self, stockamount, ticker):
        if self.cash >= stockamount * stock(price) #I couldn't determine how this works. It gives me error.
            self.cash -= stockamount * stock(price) #Same error works for here. I could not make Python calculate this calculation.
            stock.stocksinport += stockamount #For example i have used stock.stocksinport instead of stock(stocksinport) but it doesnt work either way
            self.hist.append(f"{stockamount} shares of {stock(ticker)} are bought."))
        else:
            print ("Not enough funds.")


    def history(self):
        for transaction in self.hist:
            print(transaction)


# HW1 Instructions
myportfolio = Portfolio()
myportfolio.addCash(300.50)
s = Stock(20, "HFH")
myportfolio.buyStock(5, s)
mf1 = mutualfund(0, "BRT")
mf2 = mutualfund(0, "GHT")
myportfolio.buyMutualFund(10.3, mf1)
myportfolio.buyMutualFund(4, mf2)
myportfolio.sellMutualFund(3, "BRT")
myportfolio.sellStock(1, "HFH")
myportfolio.withdrawCash(50)
myportfolio.history()
print(myportfolio)





