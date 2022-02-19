
def generateParenthesis(n):
    """
    n: 需要有几对括号
    """

    def is_legal(parentheses):
        left_count = sum([1 for p in parentheses if p == '('])
        right_count = sum([1 for p in parentheses if p == ')'])

        if (left_count < right_count) or (left_count > n):
            return False
        
        return True


    res = []
    def traceback(remain, idx, status):
        nonlocal res

        if remain == 0:
            res.append("".join(status))
            return

        for i in range(idx, 2 * n):
            status[i] = ")"
            current_part = status[: i + 1]
            if is_legal(current_part):
                traceback(remain - 1, i + 1, status)
            status[i] = "("
    
    traceback(n, 0, ["("] * 2 * n)
    return res

print(generateParenthesis(3))


        

