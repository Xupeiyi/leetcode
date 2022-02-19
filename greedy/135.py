# --------------------------------------------------------
# first try: failed
# 思路： 对于一个递增的序列，每次 分发的糖果数比之前的+ 1即可
# 对于一个长度为n的递减的序列，至少要分配 n + n-1 + n-2 + ... + 1 个糖果
# 所以， 如果 首个元素大于 n, 则除首元素外其他元素 + 1， 否则 所有元素 + 1
# 比如， 如果当前给每个孩子分配的糖果数为[4, 1]， 下一次分配糖果的数量为[4, 2, 1]， 再下一次为[4, 3, 2, 1].
# n = 5时， 5 < 4， 故分配数变为[5, 4, 3, 2, 1]
# 但这个算法无法正确处理 非严格递减的情况。 对于[1， 3， 2， 2， 1], 应该给哪个2分配更多的糖果呢？
# 因为不知道后面的数字是什么，所以根本无法判断应该当作 ratings[i] < ratings[i-1] 还是 ratings[i] > ratings[i-1]的情况
# 这个时候就可以意识到既然单纯地从前向后遍历无法解决问题，可以再试着从后向前遍历

class Solution1:
    # a wrong solution
    def candy(self, ratings) -> int:
        sum_ = 1
        prev = 1
        start = 0
        start_num = prev
        for i in range(1, len(ratings)):
            if ratings[i] < ratings[i-1] or (ratings[i] == ratings[i-1] and prev > 1):
                add = (i - start) + (i - start >= start_num)  # 如果 首个元素大于 n, 则除首元素外其他元素 + 1， 否则 所有元素 + 1
                sum_ += add
                prev = 1
            elif ratings[i] > ratings[i-1] or (ratings[i] == ratings[i-1] and prev == 1):
                prev += 1
                sum_ += prev
                start = i
                start_num = prev

        return sum_


class Solution:
    def candy(self, ratings) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        return sum(candies)


if __name__ == '__main__':
    s = Solution()
    ans = s.candy([1, 2, 3, 4])
    print(ans == 10)

    ans = s.candy([1, 0, 2])
    print(ans == 5)

    ans = s.candy([1, 2, 2])
    print(ans == 4)

    ans = s.candy([4, 5, 8, 5, 4, 3])
    print(ans == 13)
    
    ans = s.candy([1, 3, 2, 2, 1])
    print(ans == 7)
    
    ans = s.candy([29,51,87,87,72,12])
    print(ans == 12)