def to_list(n):
    return [int(char) for char in str(n)]


def to_n(num_list):
    l = len(num_list)-1
    return sum(num_list[i]*10**(l-i)for i in range(l+1))
    
    
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = to_list(n)

        digits = [nums[0]]
        for i, num in enumerate(nums[1:], 1):
            if num >= nums[i-1]:
                digits.append(num)
            else:
                break

        if len(nums) > len(digits):
            for i in range(len(digits)-1, -1, -1):
                digits[i] -= 1
                if i == 0 or digits[i] >= digits[i-1]:
                    break
                else:
                    digits[i] = 9
        
        return to_n(digits + [9] * (len(nums) - len(digits)))
        

if __name__ == '__main__':
    s = Solution()
    res = s.monotoneIncreasingDigits(12345)
    print(res)
    
    res = s.monotoneIncreasingDigits(32123)
    print(res)
    
    res = s.monotoneIncreasingDigits(2654)
    print(res)
    
    res = s.monotoneIncreasingDigits(90)
    print(res)

    