# original
def isPalindrome(s: str) -> bool:
    s = [char.lower() for char in s if char.isalnum()]
    
    left, right = 0, len(s) - 1
    while(left < right):
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))

# 原始解法中为了去除空格等特殊字符的影响先遍历一次字符串，选出字母和数字。
# 这一定程度上影响了效率，使用了额外的空间。（执行消耗内存仅超过6%用户）
# 可以在原回文串上直接判断。
def isPalindrome2(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right:
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
    return True

# 这样便在空间复杂度上超越了98%的用户。