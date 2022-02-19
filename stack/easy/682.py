def calPoints(ops) -> int:
    stack = []
    for op in ops:
        if op == '+':
            e = stack[-1] + stack[-2]
            stack.append(e)
        elif op == 'D':
            e = stack[-1] * 2
            stack.append(e)
        elif op == 'C':
            stack.pop()
        else:
            e = int(op)
            stack.append(e)
    return sum(stack)

ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))