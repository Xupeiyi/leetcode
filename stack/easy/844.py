def eliminate_backspace(str):
    stack = []
    for s in str:
        if s == '#':
            if stack != []:
                stack.pop()
        else:
            stack.append(s)
    return ''.join(stack)

def backspaceCompare(S, T) -> bool:
    S_no_backspace = eliminate_backspace(S)
    T_no_backspace = eliminate_backspace(T)
    return S_no_backspace == T_no_backspace

S, T = 'a##c', '#a#c'
print(backspaceCompare(S, T))