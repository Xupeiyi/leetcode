def build_roman_dict(char1, char5, char10):
    roman_dict = {i: char1*i for i in range(0, 4)}
    roman_dict[4] = char1 + char5
    roman_dict.update({i: char5 + char1*(i-5) for i in range(5, 9)})
    roman_dict[9] = char1 + char10
    return roman_dict
    

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        roman_dicts = [build_roman_dict('I', 'V', 'X'),
                       build_roman_dict('X', 'L', 'C'),
                       build_roman_dict('C', 'D', 'M'),
                       {i: 'M'*i for i in range(4)}]
        i = 0
        while True:
            mod = num % 10
            num = num // 10
            ans.append(roman_dicts[i][mod])
            i += 1
            
            if num == 0:
                break
        return "".join(reversed(ans))
        
        
if __name__ == '__main__':
    ans = build_roman_dict('I', 'V', 'X')
    print(ans)
    ans = build_roman_dict('X', 'L', 'C')
    print(ans)
    ans = build_roman_dict('C', 'D', 'M')
    print(ans)
    
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))