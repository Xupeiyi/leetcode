from typing import List
from math import inf

# 为什么使用哈希表：
# 1) 哈希表可以快速判断list2[i]是否在list1中, 用于找出共同喜爱的餐厅。 
# 2) 哈希表可以获取list2[i]在list1中的位置，用于计算索引和
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        positions = {restaurant: i for i, restaurant in enumerate(list1)}
        min_idx_sum, ans = inf, []
        for i, restaurant in enumerate(list2):
            if restaurant in positions:
                idx_sum = i + positions[restaurant]
                if idx_sum < min_idx_sum:
                    min_idx_sum = idx_sum
                    ans = [restaurant]
                elif idx_sum == min_idx_sum:
                    ans.append(restaurant)
        return ans