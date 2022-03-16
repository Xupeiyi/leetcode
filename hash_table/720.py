from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True
    
    def __contains__(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            if not node.is_end:
                return False
        return node.is_end


class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        for word in words:
            t.insert(word)
        max_word = ""
        for word in words:
            if word in t:
                if len(word) > len(max_word) or (len(word) == len(max_word) and word < max_word):
                    max_word = word
        return max_word


if __name__ == '__main__':
    s = Solution()
    words = ["w","wo","wor","worl","world"]
    print(s.longestWord(words))
    words = ["a","banana","app","appl","ap","apply","apple"]
    print(s.longestWord(words))
    words = ["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"]
    print(s.longestWord(words))