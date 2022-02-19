# original
from collections import Counter

def canConstruct0(ransomNote: str, magazine:str) -> bool:
    r_count = Counter(ransomNote)
    m_count = Counter(magazine)

    for letter, r_num in r_count.items():
        m_num = m_count.get(letter, 0)
        if m_num < r_num:
            return False
    
    return True

# 其实不需要把ransom中的字符数也全数一遍再比较。
# 也许在ransom数到一半时，magazine中的字符就已经不够用了。

def canConstruct1(ransomNote: str, magazine:str) -> bool:
    m_count = Counter(magazine)

    for letter in ransomNote:
        if letter not in m_count:
            return False
        else:
            m_count[letter] -= 1
            if m_count[letter] < 0:
                return False
    
    return True

print(canConstruct1("a", "b"))
print(canConstruct1("aa", "aab"))

