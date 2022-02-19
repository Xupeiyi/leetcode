class Solution:
    def sortedSquares(self, nums):
        length = len(nums)
        if length <= 1:
            return [n**2 for n in nums]
        
        res = []
        i, j = 0, length-1
        squares = [n**2 for n in nums]
        for k in range(length-1, -1, -1):
            if squares[i] >= squares[j]:
                res.insert(0, squares[i])
                i += 1
            else:
                res.insert(0, squares[j])
                j -= 1
 
        return res
    
    
if __name__ == '__main__':
    s = Solution()
    ip = [-5, -3, -2, -1, -1]
    print(s.sortedSquares(ip))


