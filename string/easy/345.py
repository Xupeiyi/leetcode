def is_vowel(char):
    return char in {"a", "e", "i", "o", "u"}


def reverseVowels(s: str) -> str:
    s_list = [char.lower() for char in s]
    left, right = 0, len(s) - 1
    while (left < right):
        left_is_vowel = is_vowel(s[left])
        right_is_vowel = is_vowel(s[right])
        
        if left_is_vowel and right_is_vowel:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        
        if not left_is_vowel:
            left += 1
        
        if not right_is_vowel:
            right -= 1
    
    result = "".join(s_list)
    return result

# 双指针从两侧向中间靠拢。


# print(reverseVowels("hello"))
print(reverseVowels("leetcode"))
