def rightmost_same_color(colors, start):
    i = start
    while i + 1 < len(colors):
        if colors[i+1] == colors[i]:
            i += 1
        else:
            break
    return i


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        chances = [0, 0]
        start = 0
        color = 0
        while start < len(colors):
            end = rightmost_same_color(colors, start)
            if (end - start) >= 2:
                chances[color] += (end - start - 1)
            color = (color + 1) % 2
            start = end + 1
        alice, bob = (0, 1) if colors[0] == 'A' else (1, 0)     
        print(chances)     
        return chances[alice] > chances[bob]


if __name__ == '__main__':
    s = Solution()
    ans = s.winnerOfGame('AAABABB')
    print(ans == True)