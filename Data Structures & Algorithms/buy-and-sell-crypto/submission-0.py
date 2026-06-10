class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize min_price to infinity so any first price will be smaller
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the lowest price seen so far
            if price < min_price:
                min_price = price
            # Calculate potential profit if sold today and update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit