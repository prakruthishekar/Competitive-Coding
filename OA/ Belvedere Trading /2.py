# Concert Ticket Exchange
# Programming challenge description:
# Concert tickets can be hard to come by, especially when going through the 
# resale market. We would like to build our own concert ticket exchange system
# so that we can view available tickets in real-time. This system will listen to
# incoming ticket orders for a new concert venue, BT Arena. We'd like to build a 
#     system that listens to concert ticket orders and provides fans with this market 
#     information in the form of a price ladder.

# Concert ticket orders arrive as a stream of events that can either add an order 
# to our market data book or delete an order from our book. We also want to be able
# to delete all orders at given price level.

# Add orders come with the following information:

# Action - ADD
# OrderId - unique identifier for order
# Artist - concert performer, such as "TaylorSwift" or "Drake"
# Price - price for the order
# quantityity - positive quantity is a buy order and negative quantity is a sell order
# Delete orders come with the following information:

# Action - DEL
# Artist - concert performer, such as "TaylorSwift" or "Drake"
# OrderId - Unique identifier for the order to be deleted
# Delete price levels come with the following information:

# Action - DEL_PRICE
# Artist - concert performer, such as "TaylorSwift" or "Drake"
# Price - price level to be deleted
# We'd like to keep track of these events so that fans can request 
# a market view in the form of a price ladder. A price ladder is made
# up of n price levels for buy orders and sell orders. A price level 
# consists of the Price, Buyquantity, and Sellquantity. A price level 
# will either have a non-zero Buyquantity or Sellquantity, but not both. 
# For buy orders, the best price is the highest price because that is the
# price a ticket holder would sell at. Conversely, the best price for sell 
# orders is the lowest price. The streamed events will guarantee at least n
# price levels for both buys and sells.

# Input:
# Repeated number of order operations in the following format:

# <ADD> <OrderId> <Artist> <Price> <quantity>
# <DEL> <OrderId> <Artist>
# <DEL_PRICE> <Artist> <Price>

# We can get orders for different artists in the same stream of operations.
#    The last line of input will the artist and number of price levels that
# we would like to view in our ladder for both buy and sell orders.

# <Artist> <NumberOfPriceLevels>

# Example Input:

# ADD 1 TaylorSwift 100 10
# ADD 2 TaylorSwift 101 -10
# ADD 3 TaylorSwift 99 5
# ADD 4 TaylorSwift 102 -5
# ADD 5 TaylorSwift 100 2
# ADD 6 Drake 95 2
# DEL 1 TaylorSwift
# TaylorSwift 2

# Output:
# The price ladder should begin with the artist name and should be followed by a 
# repeated list of levels.

# <Artist>
# <Buyquantity> <Price> <Sellquantity>

# The levels should be sorted by price in descending order and contain 
# NumberOfPriceLevels for buy and sell orders. Levels with 0 Buyquantity 
# and 0 Sellquantity should not be printed.

# Example Output:

# TaylorSwift
# 0 102 5
# 0 101 10
# 2 100 0
# 5 99 0

# Test 1
# Test Input
# Download Test 1 Input
# ADD 1 TaylorSwift 100  10
# ADD 2 TaylorSwift 101 -10
# ADD 3 TaylorSwift 99   5
# ADD 4 TaylorSwift 102 -5
# ADD 5 TaylorSwift 100  2
# DEL 1 TaylorSwift
# TaylorSwift 2
# Expected Output
# Download Test 1 Output
# TaylorSwift
# 0 102 5
# 0 101 10
# 2 100 0
# 5 99 0
# Test 2
# Test Input
# Download Test 2 Input
# ADD 1 TaylorSwift 100  10
# ADD 2 TaylorSwift 101 -10
# ADD 3 TaylorSwift 99   5
# ADD 4 TaylorSwift 102 -5
# ADD 5 TaylorSwift 98 2
# ADD 6 TaylorSwift 99   5
# DEL_PRICE TaylorSwift 100
# TaylorSwift 1
# Expected Output
# Download Test 2 Output
# TaylorSwift
# 0 101 10
# 10 99 0



import sys
import math
from collections import defaultdict
# Data classes
class AddOrder():
    def __init__(self, orderId, artist, price, quantity):
        self.orderId = int(orderId)
        self.artist = str(artist)
        self.price = float(price)
        self.quantity = float(quantity)

class ModifyOrder():
    def __init__(self, orderId, artist, price, quantity):
        self.orderId = int(orderId)
        self.artist = str(artist)
        self.price = float(price)
        self.quantity = float(quantity)
        
class DeleteOrder():
    def __init__(self, orderId, artist):
        self.orderId = int(orderId)
        self.artist = str(artist)
        
class DeletePriceLevel():
    def __init__(self, artist, price):
        self.artist = str(artist)        
        self.price = int(price)

# TODO(candidate): implementation below
class PriceLadder():
    def __init__(self):
        self.buyOrders = defaultdict(lambda: defaultdict(float))
        self.sellOrders = defaultdict(lambda: defaultdict(float))
        self.orderToPrice = {}
    
    def AddOrder(self, order):
        #  TODO(candidate): implement
        artist = order.artist
        price = order.price
        quantity = order.quantity
        orderId = order.orderId
        if quantity > 0:
            self.buyOrders[artist][price] += quantity
        else:
            self.sellOrders[artist][price] -= quantity
        self.orderToPrice[orderId] = (artist, price, quantity)
        
    def DeleteOrder(self, delete):
        # TODO(candidate): implement
        artist, price, quantity = self.orderToPrice[delete.orderId]
        if quantity > 0:
            self.buyOrders[artist][price] -= quantity
        else:
            self.sellOrders[artist][price] += quantity
        del self.orderToPrice[delete.orderId]
    
    def DeletePriceLevel(self, deletePriceLevel):
        # TODO(candidate): implement
        self.buyOrders[deletePriceLevel.artist].pop(deletePriceLevel.price, None)
        self.sellOrders[deletePriceLevel.artist].pop(deletePriceLevel.price, None)
    
    def GetPriceLevels(self, artist, numberOfPriceLevels):
        # TODO(candidate): implement
        print(artist)
        combined_levels = []
        for price, quantity in sorted(self.buyOrders[artist].items(), reverse=True)[:numberOfPriceLevels]:
            combined_levels.append((quantity, price, 0))
        for price, quantity in sorted(self.sellOrders[artist].items())[:numberOfPriceLevels]:
            combined_levels.append((0, price, quantity))
        
        for level in sorted(combined_levels, key=lambda x: -x[1]):
            if level[0] != 0 or level[2] != 0:
                print(int(level[0]), int(level[1]), int(level[2]))

priceLadder = PriceLadder()
for line in sys.stdin:
    tokens = line.split()
    if tokens[0] == "ADD":
        priceLadder.AddOrder(AddOrder(*tokens[1:]))
    elif tokens[0] == "DEL":
        priceLadder.DeleteOrder(DeleteOrder(*tokens[1:]))
    elif tokens[0] == "DEL_PRICE":
        priceLadder.DeletePriceLevel(DeletePriceLevel(*tokens[1:]))
    else:
        artist = tokens[0]
        numberOfPriceLevels = int(tokens[1])
        priceLadder.GetPriceLevels(artist, numberOfPriceLevels)