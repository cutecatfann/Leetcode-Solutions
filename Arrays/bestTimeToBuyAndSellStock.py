class Solution:
    def maxProfit(self,prices):
        left = 0 # looks for the lowest buy point
        right = 1 # looks for the highest sell point
        maxProf = 0
        
        while right < len(prices):
            currentProfit = prices[right] - prices[left] # gets current profit by subtracting pointers
            if prices[left] < prices[right]: # checks for a new max profit
                maxProf = max(currentProfit,maxProf)
            else:
                left = right # increases pointers to next position
            right += 1
        
        return maxProf
