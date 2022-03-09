class WordDictionary:

    def __init__(self):
        self.children = dict()
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, idx):
            nonlocal word
            if idx == len(word):
                return node.is_end

            char = word[idx]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, idx+1):
                        return True
            else:
                if char in node.children:
                    return dfs(node.children[char], idx+1)
            return False

        return dfs(self, 0)


    # def search(self, word: str) -> bool:
    #     ans = False

    #     def backtrack(root, idx):
    #         nonlocal ans, word
            
    #         if idx == len(word):
    #             if root.is_end:
    #                 ans = True
    #             return

    #         if word[idx] == '.':
    #             for child in root.children.values():
    #                 if not ans:
    #                     backtrack(child, idx+1)
    #         else:
    #             if word[idx] in root.children and not ans:
    #                 backtrack(root.children[word[idx]], idx+1)
        
    #     backtrack(self, 0)
    #     return ans


if __name__ == '__main__':
    w = WordDictionary()
    w.addWord("abxd")
    ans = w.search("ab.")
    print(ans)

    w.addWord("abf")
    ans = w.search("ab.")
    print(ans)
