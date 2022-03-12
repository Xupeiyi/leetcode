class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1 and n != -1:
            if not n % 2:
                n /= 2
            elif not n % 3:
                n /= 3
            elif not n % 5:
                n /= 5
            else:
                return False
        return True