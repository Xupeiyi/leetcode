class Solution:
    def totalFruit(self, fruits) -> int:
        length = len(fruits)
        holding = set()
        max_holding = 0
        seq_start = -1
        i = 0
        for j in range(length):
            if fruits[j] not in holding:
                
                # if cannot pick another kind of fruit
                if len(holding) >= 2:
                    max_holding = max(max_holding, j - i)
                    
                    # make i point to the first occurrence of the previous kind of fruit
                    i = seq_start
                    holding = {fruits[i]}
                    
                holding.add(fruits[j])
            
            if fruits[j] != fruits[j-1]:
                seq_start = j
            
        return max(max_holding, length - i)
        
        
if __name__ == '__main__':
    s = Solution()
    l0 = [1, 1, 2, 3, 2, 3, 2]
    l1 = [1, 2, 3, 2, 2, 4, 4, 4, 4, 4]
    l2 = [0, 1, 2, 2]
    l3 = [4, 1, 1, 1, 3, 1, 7, 5]
    print(s.totalFruit(l1))