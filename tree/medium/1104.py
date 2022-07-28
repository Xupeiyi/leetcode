from typing import List

def parent(label):
    i = len(bin(label)) - 3
    return 2 ** (i - 1) + 2 ** i - 1 - label // 2

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        ans = []
        while label >= 1:
            ans.append(label)
            label = parent(label)

        return ans[::-1]

if __name__ == '__main__':
    s = Solution()
    ans = s.pathInZigZagTree(14)
    print(ans)

    # for i in range(1, 16):
    #     print(i, parent(i))
