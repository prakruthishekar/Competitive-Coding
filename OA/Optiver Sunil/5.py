# As a trading firm Optiver trades stocks as well as many derivative instruments such as 
# options and futures. This makes it important for us to be able to calculate future prices 
# of a stock based on the market information we have. Stock prices in the future are affected 
# by dividends - which for the purpose of this problem is a fixed amount that gets paid out on 
# a particular date.


# Mathematically speaking, if today the stock price is S, and a dividend of amount 
# A is to be paid out D days from now, then:
# • Future price from today till day D - 1 is S
# • Future price from day D onwards (including D) is S - A
# Naturally, if there are multiple dividends this has an additive effect. Consider
#  the following example:
# Say the stock price today is S = 1000, and there are 2
# dividends:
# • (1) A, = 100, D, = 10 days tAm now,
# • (2) A2 = 50, D2 = 100 days from now.
# Then the future prices varies as follows:
# • 1000 from Day 0 (today) to Day 9.
# • 900 (= 1000-100) from Day 10 to Day 99.
# •850 (= 1000-100-50) from Day 100 onwards.

# Problem Statement
# In this problem, you will be given today's stock price S, and N dividends
#  - each with an amount A and' day D; from today (1 ≤ i≤ N) as input.
# You will also be asked to perform Q operations. Each operation can be an update or a query.
# There is only 1 kind of update:
# • DIVIDEND_UPDATE(i, A, D) - indicates that ith dividend should be updated 
# from (A;, Di) to (A, D).
# There is only 1 kind of query:
# • PRICE(F) - output the future price on day F based on all N dividends.
# Function Description
# Your task is to implement a class that
# provides UpdateDividend and CalculateFuturePrice methods.


# Input Format For Custom Testing
# ALL
# 2
# Input to the program is specified using a simple text format. The format and 
# details of parsing are not relevant to answering the question but custom input can be 
# used to help with development and debugging.
# The first line contains 3 integers: S, N and Q. The next N lines each contain 2 integers 
# - A; and D; (1 < iS N) indicating dividend amounts and dates. Each of the Q subsegent lines 
# contains either an update or a query in the format below:
# Updates:
# • DIVIDEND UPDATE < <Amount> <Days>
# Query:
# • PRICE <Days>
# For each PRICE query, output the future price on a new line.


# Sample Case 1
# Sample input for custom testing:
# 1000 2 4
# 100 10
# 50 100
# PRICE 15
# DIVIDEND_ UPDATE 2 40 20
# PRICE 15
# PRICE 25


# Expected output:
# 900
# 900
# 860


from dataclasses import dataclass


@dataclass
class Dividend:
    amount: int
    days: int


class FuturePricingEngine:
    def __init__(self, stock_price: int, dividends: list[Dividend]):
        self.stock_price = stock_price
        self.dividends = sorted(dividends, key=lambda x: x.days)  # Sorting by days

    def update_dividend(self, dividend_id: int, updated_dividend: Dividend):
        self.dividends[dividend_id - 1] = updated_dividend
        self.dividends.sort(key=lambda x: x.days)  # Sorting again after update

    def calculate_future_price(self, days_to_future: int) -> int:
        price = self.stock_price
        for dividend in self.dividends:
            if days_to_future >= dividend.days:
                price -= dividend.amount
        return price


# Sample usage
if __name__ == "__main__":
    stock_price = 1000
    dividends = [Dividend(100, 10), Dividend(50, 100)]
    pricing_engine = FuturePricingEngine(stock_price, dividends)

    print(pricing_engine.calculate_future_price(15)) # Output: 900

    pricing_engine.update_dividend(2, Dividend(40, 20))
    print(pricing_engine.calculate_future_price(15)) # Output: 900
    print(pricing_engine.calculate_future_price(25)) # Output: 860
