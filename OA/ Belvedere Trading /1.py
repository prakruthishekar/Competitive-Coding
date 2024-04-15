# Programming challenge description:
# When a trader buys or sells an asset, that trade is said to have a certain 
# amount of "edge" defined as the difference between the trade price and a 
# theoretical value. Theoretical value is what the Trader or Firm thinks the 
# asset is worth, and can change throughout the day.

# Edgebuy  = TheoreticalValue − TradePrice
# Edgesell = TradePrice − TheoreticalValue

# Traders typically want to execute trades that have positive edge, that is 
# buying an asset for lower than the theoretical value, or selling an asset 
# for higher than the theoretical value.

# For example: TradePrice = 95, TheoreticalValue = 100, Edge = 100-95 = 5

# As a Firm, we want to track which traders are making the best decisions, 
# so we calculate a score for each trade.

# Score= SignOfEdge(Edge^​2 ∗∣Quantity∣)


# Notice that negative edge will result in a negative score, indicating a bad trade.

# Task
# Given a series of trades, print the trader with the highest cumulative score after
#  each trade.

# Additional Details
# A "Buy" trade will have positive quantity, and "Sell" trades will be denoted by
# negative (-) quantity.

# Theoretical Values can be updated periodically. Your solution should use the most 
# recent theoretical value when calculating edge. If an asset does not have an available
# theoretical value at the time of trade, assume Edge = 0 and save the trade price
# as the theoretical value. Theo Updates are not retroactive, so any existing trade
# for that asset should NOT be updated

# Trades may happen with negative edge. They are valid and should be included in
#  a traders cumulative score.

# If more than one trader has the highest cumulative score, use lexicographical 
# ordering of TraderName to break the tie.

# Input:
# A number trade lines in the following format:

# Trade <TraderName> <Asset> <Quantity> <Price>

# Interlaced with 1 or more theo update lines in the following format:

# TheoUpdate <Asset> <Value>

# Example:

# TheoUpdate 1 100
# Trade Alice 1 1 95
# Trade Bob 1 1 94
# Trade Alice 1 -1 107
# Output:
# A line of output for each trade in the input, in the format

# Example:

# Alice 25
# Bob 36
# Alice 74
# Test 1

# Test Input

# TheoUpdate 1 100
# Trade Alice 1 1 95
# Trade Bob 1 1 94
# Trade Alice 1 -1 107


# Expected Output
# Download Test 1 Output
# Alice 25.00
# Bob 36.00
# Alice 74.00




import sys
from collections import defaultdict


class Trade():
    def __init__(self, trader, asset, quantity, price):
        self.Trader = trader
        self.Asset = asset
        self.Quantity = quantity
        self.Price = price
    
class TheoUpdate():
    def __init__(self, asset, value):
        self.Asset = asset
        self.Value = value

def ParseTrade(line):
    args = line.split(" ")
    return Trade(str(args[1]), int(args[2]), int(args[3]), float(args[4]))

def ParseTheoUpdate(line):
    args = line.split(" ")
    return TheoUpdate(int(args[1]), float(args[2]))

def PrintTraderScore(traderName, score):
    print(traderName, "{:.2f}".format(score)) 

class TradeAggregator():
    def __init__(self):
        self.theo_values = defaultdict(float)
        self.trader_scores = defaultdict(float)
    def HandleTrade(self, trade):
        theoretical_value = self.theo_values.get(trade.Asset, trade.Price)
        if trade.Asset not in self.theo_values:
            self.theo_values[trade.Asset] = trade.Price
        edge = (theoretical_value - trade.Price) if trade.Quantity > 0 else (trade.Price - theoretical_value)
        sign_of_edge = 1 if edge >= 0 else -1
        score = sign_of_edge * (edge ** 2) * abs(trade.Quantity)
        self.trader_scores[trade.Trader] += score
    def HandleTheoUpdate(self, theoUpdate):
        self.theo_values[theoUpdate.Asset] = theoUpdate.Value

    def PrintBestScore(self):
        max_score = max(self.trader_scores.values())
        best_traders = [name for name, score in self.trader_scores.items() if score == max_score]
        best_trader = min(best_traders)
        best_score = self.trader_scores[best_trader]

        PrintTraderScore(best_trader, best_score)


tradeAgg = TradeAggregator()
for line in sys.stdin:
    if line.find("Trade") != -1:
        trade = ParseTrade(line)
        tradeAgg.HandleTrade(trade)
        tradeAgg.PrintBestScore()
    else:
        theoUpdate = ParseTheoUpdate(line)
        tradeAgg.HandleTheoUpdate(theoUpdate)
 