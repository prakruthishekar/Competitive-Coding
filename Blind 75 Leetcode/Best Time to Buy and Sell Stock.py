
class Solution:
    def maxProfit(self,prices):
        min = prices[0]
        profit = 0
        for i in range(len(prices)):
            if(prices[i]< min):
                min = prices[i]
            profit = max(profit, prices[i]-min)
        
        return(profit)

prices  = [7,1,5,3,6,4]
classObject = Solution() 
print(classObject.maxProfit(prices))    