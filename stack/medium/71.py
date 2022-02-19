def simplifyPath(path):
    dirs = [d for d in path.split('/') if d]
    
    stack = []
    for d in dirs:
        if d == '.':
            pass
        elif d == '..':
            if stack:
                stack.pop()
        else:
            stack.append(d)
    return '/' + '/'.join(stack)

'''
performance
time  78.51  91.38  91.38  78.51  56.78
space 5.92   10.11  10.11  25.98  23.33
'''


path = '/a/./b/../../c/'
print(simplifyPath(path))