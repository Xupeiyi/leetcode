class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: (x[0], -x[1]))
        ans = []
        for person in reversed(people):
            ans.insert(person[1], person)
        return ans
        
        
if __name__ == '__main__':
    s = Solution()
    p = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    s.reconstructQueue(p)
