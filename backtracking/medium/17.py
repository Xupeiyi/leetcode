# --------------------------------------
# Solution 1
from itertools import product

num_to_letter = {
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'h', 'i'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'],
    "7": ['p', 'q', 'r', 's'],
    "8": ['t', 'u', 'v'],
    "9": ['w', 'x', 'y', 'z']
}


def letterCombinations(digits):
    if not digits:
        return []
    combinations = product(*[num_to_letter[s] for s in digits])
    combinations = ["".join(c) for c in combinations]
    return combinations


# ------------------------------------
# Solution2

class Solution:
    def letterCombinations(self, digits: str):
        ans = []
        
        def backtrack(rest, path):
            if rest == "":
                ans.append(path)
                return
            
            for char in num_to_letter[rest[0]]:
                backtrack(rest[1:], path+char)
        
        if digits:
            backtrack(digits, "")

        return ans
        
        
if __name__ == '__main__':
    print(letterCombinations("2"))
    s = Solution()
    ans = s.letterCombinations("2")
    print(ans)