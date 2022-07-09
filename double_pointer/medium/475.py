import math
import bisect
from typing import List

from black import main


class Solution0:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        min_radius = 0
        houses = sorted(houses)
        heaters = sorted(heaters)
        heaters = [-math.inf] + heaters + [math.inf]
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            radius = min(heaters[idx] - house, house - heaters[idx-1])
            min_radius = max(radius, min_radius)
        return min_radius


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        min_radius = 0
        houses = sorted(houses)
        heaters = sorted(heaters)
        heaters = [-math.inf] + heaters + [math.inf]
        idx = 0
        for house in houses:
            while heaters[idx] <= house:
                idx += 1
            radius = min(heaters[idx] - house, house - heaters[idx-1])
            min_radius = max(radius, min_radius)
        return min_radius


if __name__ == '__main__':
    s = Solution()
    houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
    heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
    ans = s.findRadius(houses, heaters)
    print(ans)