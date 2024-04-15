# Opportunistic Stock Trading
# Programming challenge description:
# Background
# Your brokerage firm notices that individual investors only like to trade the 
# big-name stocks. To make lesser-known stocks appealing, they start allowing users
# to buy multiple different stocks in “bundles” in their account. This means that 
# they may offer a bundle which contains 1 BBBY stock, 1 AAPL stock, and 1 GOOG stock 
# all as one package. Bundles may also contain other bundles.

# Being the sophisticated investor that you are, you notice that sometimes your 
# brokerage misprices their bundles relative to the price of the individual stocks 
# (and vice-versa). The same bundle above has been priced at $100 even though AAPL 
# stock is trading for $35, BBBY for $34, and GOOG for $40 which means the bundle 
# should be priced at $109. So, you buy the bundle and save yourself $9!

# You have cracked the code and now want to find as many opportunities like this as 
# you can!

# Additional Notes
# A bundle may contain a stock/sub-bundle which does not exist because it is not 
# listed at that particular venue. In this case, you must pass on trading the bundle.
# If a bundle A contains bundle B and bundle B contains stock C which is not listed, 
# then neither B nor A can be purchased. They both must be passed.
# Specifying Bundle vs. Individual only applies to the top-level bundle vs any
# combination of it's individual components (whether or not a sub-bundle can be
# optimally purchased at the bundle price vs individual stocks is not important)
# A bundle cannot include a bundle which already includes it in its listing. Ie. 
# no circular listing
# You can't replicate a bundle by buying a bundle which contains separate stocks. 



# For example, if a bundle b1 contains {AAPL, META, TSLA} you cannot buy the bundle
#  b2 containing {AAPL, META, GOOG} + a TSLA share + sell the GOOG stock even if it 
#  yields a more optimal price
# Input:


# A set of stock bundle symbols (should try to trade in the order they are inputted)
# For each bundle in the market:
# The bundle symbol
# The price of the bundle
# The number of stocks/sub-bundles which make up the bundle
# A list of {stock symbol, quantity} pairs which make up the bundle
# For each individual stock in the market:
# The product symbol
# The price to purchase the product


# Input format example:
# <number_of_bundles_to_trade>, <number_of_stocks>
# <bundle_symbol>,<price_to_purchase>,<num_stocks>,<{stock_symbol, quantity}> 
# <bundle_symbol>,<price_to_purchase>,<num_stocks>,<{stock_symbol, quantity}>
# <stock_symbol>,<price_to_purchase>
# <stock_symbol>,<price_to_purchase>
# <stock_symbol>,<price_to_purchase>


# 5 8
# apx 100 4 aapl 3 amzn 4 aarp
# spj 145 5 spy 2 slrp 4 szzl 1 stp 2 swg
# sspx 30 1 spy 1 slrp
# dpx 900 2 apx 5 spj
# spdx 30 2 aapl  1 spy
# ctt 600 55 aapl 2 spy
# aapl 10
# amzn 10
# aarp 10
# spy 10
# slrp 10
# szzl 10
# stp 10
# swg 10


# Output:
# For each stock bundle provided in the input, you should output whether you
# bought the bundle or individual stocks and what the cost of the transaction was. 
# If there is no arbitrage opportunity, you must pass on the trade.

# Output format example:
# <bundle_symbol>, <execute_or_pass>, <bundle_or_individual_stocks>, <total_price>

# apx E B 100.0
# spj E I 130.0
# sspx E I 20.0
# dpx E B 900.0
# spdx P /* no arbitrage opportunity */


# Test 1

# 3 5
# apx 99.5 3 aapl 4 amzn 3 aarp 4
# spj 200.0 2 spy 3 swg 2
# sspx 65 2 spy 1 aapl 1
# aapl 10.5
# amzn 12.0
# aarp 5.0
# spy 45.0
# swg 33.5

# Expected Output

# apx E I 98.00
# spj E B 200.00
# sspx E I 55.50

# Test 2
# Test Input
# 2 4
# adgb 5404.0 3 tadb 2 goog 2 meta 1
# tadb 2520.0 2 bbby 5 hmny 4
# goog 125.0
# meta 114.0
# bbby 225.0
# hmny 350.75

# Expected Output
# adgb P
# tadb E B 2520.00



import sys

class Bundle:
    def __init__(self, name, price, components):
        self.name = name
        self.price = price
        self.components = components

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def PrintTrade(name, bundleOrStock, price):
    p = "{:.2f}".format(price)
    print("{} E {} {}".format(name, bundleOrStock, p))

def PrintNoTrade(name):
    print("{} P".format(name))

class MarketWatchPortfolio:
    def __init__(self, bundles, stocks):
        self.bundles = bundles
        self.stocks = stocks
        
    def calculate_bundle_price(self, components, visited_bundles):
        price = 0
        for quantity, name in components:
            if name in self.stocks:
                price += quantity * self.stocks[name].price
            else:
                sub_bundle = next((b for b in self.bundles if b.name == name), None)
                if sub_bundle:
                    if name in visited_bundles:
                        return float('inf') # Circular reference, return inf
                    visited_bundles.add(name)
                    sub_bundle_price = self.calculate_bundle_price(sub_bundle.components, visited_bundles.copy())
                    if sub_bundle_price < sub_bundle.price:
                        price += quantity * sub_bundle_price
                    else:
                        return float('inf') # Sub-bundle is not mispriced, return inf
                else:
                    return float('inf') # Component not found, return inf
        return price



    def ExecuteTrades(self):
        for bundle in self.bundles:
            visited_bundles = set()
            individual_price = self.calculate_bundle_price(bundle.components, visited_bundles)
            if individual_price < float('inf'):
                if individual_price < bundle.price:
                    PrintTrade(bundle.name, 'I', individual_price)
                else:
                    PrintTrade(bundle.name, 'B', bundle.price)
            else:
                PrintNoTrade(bundle.name)


def ParseInputs():
    bundles = list()
    stocks = dict()
    num_stocks = -1
    num_bundles = -1
    for line in sys.stdin:
        parsed = line.strip().split(' ')
        if num_bundles == -1 and num_stocks == -1:
            num_bundles = int(parsed[0])
            num_stocks = int(parsed[1])
            continue
        if num_bundles > 0:
            components = list()
            for i in range(3, len(parsed) - 1, 2):
                components.append((int(parsed[i + 1]), parsed[i]))
            bundles.append(Bundle(parsed[0], float(parsed[1]), components))
            num_bundles -= 1
            continue
        s = Stock(parsed[0], float(parsed[1]))
        stocks[parsed[0]] = s
    return MarketWatchPortfolio(bundles, stocks)

def main():
    portfolio = ParseInputs()
    portfolio.ExecuteTrades()

if __name__ == '__main__':
    main()