

def isValid(s: str) -> bool:
    pair = {'(': ')', '[': ']','{': '}'}
    stack = []
    
    for char in s:
        if char in pair: 
            stack.append(pair[char])
        else:
            if stack == [] or char != stack.pop(-1):
                return False
                
    return stack == []



print(isValid("()") == True)
print(isValid("()[]{}") == True)
print(isValid("(]") == False)
print(isValid("([)]") == False)
print(isValid("{[]}") == True)
print(isValid("(") == False)
print(isValid(")") == False)