def maxUniqueSplit(s):
    res = 0

    def backtrack(remain, path):
        nonlocal res

        if len(remain) + len(path) <= res:
            return

        if remain == '':
            if len(path) > res:
                res = len(path)
            return

        for i in range(len(remain)):
            cut, rest = remain[:i+1], remain[i+1:]
            if len(path | {cut}) == len(path) + 1:
                backtrack(rest, path | {cut})
        
    backtrack(s, set())
    return res

print(maxUniqueSplit("ababccc"))
print(maxUniqueSplit("aba"))