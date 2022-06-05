class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar=prices[0]
        maxprofit=0
        for price in prices[1:]:
            
            if price < minsofar:
                minsofar=price
            if maxprofit < (price-minsofar):
                maxprofit=price-minsofar
        return maxprofit