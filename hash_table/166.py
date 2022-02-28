class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 注意integer为负数的情况
        sign = '-' if (numerator * denominator < 0) else ''
        numerator = abs(numerator)
        denominator = abs(denominator)

        # 检查是否整除
        integer = str(numerator // denominator)
        decimal = sign + integer
        numerator = (numerator % denominator) * 10
        if not numerator:
            return decimal
        
        # 计算小数部分，记录循环开始的位置
        decimal += '.'
        
        digits = []
        num_pos = {} 
        i = 0
        while numerator not in num_pos and numerator != 0:
            digit = numerator // denominator
            digits.append(str(digit))
            num_pos[numerator] = i
            i += 1
            numerator = (numerator % denominator) * 10

        # 添加小数部分
        if numerator in num_pos:
            recur_start = num_pos[numerator]
            decimal += ''.join(digits[0:recur_start]) + '(' + ''.join(digits[recur_start:]) + ')'
        else:
            decimal += ''.join(digits)
        return decimal


if __name__ == '__main__':
    s = Solution()
    ans = s.fractionToDecimal(-2147483648, 1)
    print(ans)