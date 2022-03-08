def pos_to_cr(pos):
    c = ord(pos[0]) - ord('A')
    r = int(pos[1])
    return c, r

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Solution:
    def cellsInRange(self, s: str):
        pos1, pos2 = s.split(":")
        c1, r1 = pos_to_cr(pos1)
        c2, r2 = pos_to_cr(pos2)
        return [letters[c] + str(r) for c in range(c1, c2+1) for r in range(r1, r2+1)]

if __name__ == '__main__':
    s = Solution()
    ans = s.cellsInRange("A1:F1")
    print(ans)