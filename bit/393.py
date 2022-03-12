from typing import List


def count_ones(num):
    if num < 128:
        return False
    bin_str = bin(num)[2:]
    ans = 0
    for char in bin_str:
        if char == '1':
            ans += 1
        else:
            return ans
    return ans


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0

        while i < n:
            # 检查数字以几个1为开始
            ones = count_ones(data[i])
            if ones < 1:
                i += 1
                continue

            elif ones == 1 or ones > 4:
                return False
            
            else:
                # 验证之后ones - 1个数都以 10 开头
                ones -= 1
                while True:
                    ones -= 1
                    i += 1

                    if not(i < n and count_ones(data[i]) == 1):
                        return False
                    
                    if not ones:
                        break
                i += 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validUtf8([235, 140, 4]))
    print(s.validUtf8([197, 130, 1])) 



                
