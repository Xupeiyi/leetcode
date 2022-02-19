def removeOuterParentheses(S):
    primitives = []
    stack = 0
    primitive = ''

    for s in S:
        if s == '(':
            stack += 1
        elif s == ')':
            stack -= 1

        primitive += s        
        if stack == 0:
            primitives.append(primitive[1:-1])
            primitive = ''
    
    return ''.join(primitives)

'''
performance
time  61   10   61   81   81
space 83   14   95   13   17
'''

S = "(()())(())(()(()))"
print(removeOuterParentheses(S))
