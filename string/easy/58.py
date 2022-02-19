def lengthOfLastWord(s:str) -> int:
    if s == '':
        return 0
    s = s.rstrip()
    words = s.split(' ')
    return len(words[-1])

print(lengthOfLastWord("hello world"))
