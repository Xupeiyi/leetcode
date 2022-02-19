# 从一开始思路就错了。
# 比如，对于价格序列[1, 3, 2, 8, 4, 9], 我想的是如何计算每一步的利润， 然后把他们加起来变成正确的。
# 思考的子问题是[1, 3], [3, 2], [8, 4], [4, 9]。
# 但实际上， 思考的范围是[1, 3], [1, 3, 2], [1, 3, 2, 8], [1, 3, 2, 8, 4], [1, 3, 2, 8, 4, 9]


class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        result = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            # 更新买入价格
            if prices[i] < min_price:
                min_price = prices[i]
            
            # 价格高于买入价，但无法弥补手续费
            elif prices[i] >= min_price and prices[i] <= min_price + fee:
                continue
            
            # 计算收益，prices-fee 以免连续计算收益时重复计算手续费
            else:
                result += prices[i] - min_price - fee
                min_price = prices[i] - fee
        return result