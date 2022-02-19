class Solution:
    def integerBreak(self, n):
        max_break = [0, 1] + [0] * (n-1)
        
        for num in range(2, n+1):
            mid = num // 2
            products = []
            for c1 in range(1, mid+1):
                c2 = num - c1
                product = max(c1, max_break[c1]) * max(c2, max_break[c2])
                products.append(product)
            max_break[num] = max(products)
            
        return max_break[-1]
    
    
if __name__ == '__main__':
    s = Solution()
    ans = s.integerBreak(10)
    print(ans)
    