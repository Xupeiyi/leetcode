class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1
        
        other = {1: 2, 2: 1}
        string = [1, 2, 2]  + [1] * (n - 3)
        fast = 3
        slow = 1
        ones = 1
        while fast < n:
            slow += 1
            value = other[string[fast-1]]
            cnt = 0
            while cnt < string[slow]:
                if fast >= n:
                    return ones
                string[fast] = value
                fast += 1
                cnt += 1
                ones += (value == 1)
        return ones

if __name__ == '__main__':
    s = Solution()
    ans = s.magicalString(4)
    print(ans)