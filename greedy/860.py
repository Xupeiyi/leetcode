class Solution:
    def lemonadeChange(self, bills) -> bool:
        five, ten = 0, 0  # $5, $10
        for b in bills:
            if b == 5:
                five += 1
            
            elif b == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            
            elif b == 20:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True