# original
def reverseString(s: list) -> None:
    left, right = 0, len(s) - 1
    while (left < right):
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return 

# 双指针从两侧到中间。并不复杂。