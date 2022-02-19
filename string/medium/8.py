MAX_INT = 2**31 - 1
MIN_INT = -2**31


class Solution:
   
    def myAtoi(self, s: str) -> int:
        ans = 0
        sign = 1
        
        # lstrip
        start = 0
        while s[start] == ' ':
            start += 1
        
        for i, char in enumerate(s[start:], start):
            if not char.isdigit():
                if i == start and char == '-':
                    sign = -1
                elif i == start and char == '+':
                    continue
                else:
                    break
            else:
                ans = ans*10 + int(char) * sign
                if ans >= MAX_INT:
                    return MAX_INT
                if ans <= MIN_INT:
                    return MIN_INT
        
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    
    print(s.myAtoi("+42") == 42)
    print(s.myAtoi("+ 42") == 0)
    print(s.myAtoi("42") == 42)
    print(s.myAtoi("0042") == 42)
    print(s.myAtoi("00 42") == 0)
    
    print(s.myAtoi("-0042") == -42)
    print(s.myAtoi("           -42") == -42)
    print(s.myAtoi("     - 42") == 0)
    print(s.myAtoi("4193 abcd") == 4193)
    print(s.myAtoi("--42") == 0)
    print(s.myAtoi("42 123") == 42)
    print(s.myAtoi("-91283472332") == MIN_INT)
    print(s.myAtoi("5147483648") == MAX_INT)
    
    print(s.myAtoi("abcd 987") == 0)
    