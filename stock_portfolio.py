class Stock:

    def __init__(self, symbol, quantity, price_per_share):
        self.symbol = symbol
        self.quantity = quantity
        self.price_per_share = price_per_share

    def value(self):
        return self.quantity * self.price_per_share

    def __str__(self):
        return f"Symbol: {self.symbol}, Quantity: {self.quantity}, Price per share: {self.price_per_share}"


class Portfolio:

    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def total_value(self):
        totalv = 0
        for stock in self.stocks:
            totalv += stock.value()
        return totalv

    def __add__(self, other):
        new_portfolio = Portfolio()
        new_portfolio.stocks = self.stocks + other.stocks
        return new_portfolio

    def __eq__(self, other):
        return self.total_value() == other.total_value()

    def __lt__(self, other):
        return self.total_value() < other.total_value()

    def __gt__(self, other):
        return self.total_value() > other.total_value()

    def __len__(self):
        return len(self.stocks)

    def __getitem__(self, item):
        for stock in self.stocks:
           if stock.symbol == item:
               return stock
        raise KeyError(f"No stock found with the symbol {item}")

    def __str__(self):
        summary = "\n".join(str(stock) for stock in self.stocks)
        return f"Portfolio Summary: \n{summary}\nTotal Value: ₹{self.total_value()}"


apple = Stock("AAPL", 10, 180)
tesla = Stock("TSLA", 5, 250)
google = Stock("GOOG", 8, 130)

portfolio1 = Portfolio()
portfolio1.add_stock(apple)
portfolio1.add_stock(tesla)

portfolio2 = Portfolio()
portfolio2.add_stock(google)

print(portfolio1.total_value())   # 10*180 + 5*250 = 3050
print(len(portfolio1))            # 2
print(portfolio1 > portfolio2)    # True or False

portfolio3 = portfolio1 + portfolio2
print(portfolio3)
