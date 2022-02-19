char_to_value = {
    'I': 1, 
    'V': 5, 
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def romanToInt(s: str) -> int:
    values = [char_to_value[char] for char in s]

    sum = 0
    for value, following_value in zip(values[:-1], values[1:]):
        if value < following_value:
            sum -= value
        else:
            sum += value
    sum += values[-1]

    return sum
   


print(romanToInt('III') == 3)
print(romanToInt('IV') == 4)
print(romanToInt('IX') == 9)
print(romanToInt('LVIII') == 58)
print(romanToInt('MCMXCIV') == 1994)
