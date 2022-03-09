# 前缀树，一棵26叉树
class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.is_end


    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert("apple")
    print(t.startsWith("app"))
    print(t.search("app"))
    print(t.search("apple"))
    print(t.search("apples"))