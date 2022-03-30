from typing import List

def num_to_list(n):
    if n == 0:
        return []

    return num_to_list(n // 10) + [(n % 10)]


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            num_list = num_to_list(i)
            for n in num_list:
                if n == 0 or i % n != 0:
                    break
            else:
                ans.append(i) 
        return ans



if __name__ == '__main__':
    s = Solution()
    print(num_to_list(99))
    print(s.selfDividingNumbers(66, 708))