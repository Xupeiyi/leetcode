from collections import Counter
from turtle import update


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        if len(text) <= 1:
            return len(text)

        count = Counter(text)
        
        substr = {text[0]: 1}
        start = 0
        for end in range(1, len(text)):
            update_window = False

            if text[end] in substr:
                if len(substr) == 2:
                    other_key = (substr.keys() - {text[end]}).pop()
                    if substr[other_key] > 1:
                        update_window = True


if __name__ == '__main__':
    s = Solution()
    s.maxRepOpt1("aabcd")