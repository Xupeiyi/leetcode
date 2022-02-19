# original
def checkPowersOfThree(n: int) -> bool:
    res = False
    def backtrack(s, power):
        """
        s: 当前总和
        power: 当前要加上的3的指数
        """

        nonlocal res
        if s == n:
            res = True
            return

        for p in range(power, 15):
            add = 3 ** p
            new_sum = s + add
            if new_sum <= n and not res:
                backtrack(new_sum, p + 1)
            else:
                break # 没有必要加上更大的add了
    
    backtrack(0, 0)
            
    return res




# 上面是从0开始往上加的办法。
# 如果换成从n开始往下减？
def three_powers_le(n):
    three_powers = []
    i = 0
    while 3 ** i <= n:
        three_powers.append(3 ** i)
        i += 1
    return three_powers


def checkPowersOfThree2(n: int) -> bool:
    three_powers = three_powers_le(n)  # 第 i 个元素为 3**i, 所有元素小于等于n
    cumsum_three_powers = [0.5*(3**(i+1)-1) for i in range(0, len(three_powers))]    # 第 i 个元素为 3**0 + 3**1 + ... + 3**i

    ans = False
    def backtrack(number, power):
        """
        number: 当前被减数
        power: 当前要减去的3的幂。
        """
        nonlocal ans

        if number == 0:
            ans = True
            return
        
        for p in range(power, -1, -1):
            # 如果 number 大于 3**0 + ... + 3**p，则必定不可能表示为3的幂的和
            # 比如，3**4 > 41 > 3**3 + 3**2 + 3**1 + 3**0, 则可知41不可能为3的幂的和            
            if number > cumsum_three_powers[p]:
                break
            
            rest = number - three_powers[p]
            if rest >= 0 and not ans:
                backtrack(rest, p - 1)
   
    backtrack(n, len(three_powers) - 1)
    return ans

# print(checkPowersOfThree2(12))
print(checkPowersOfThree2(41))
print(checkPowersOfThree2(6378022))