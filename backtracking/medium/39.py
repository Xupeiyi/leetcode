def combinationSum(candidates, target):
    res = []
    
    def backtrack(remain, path):
        nonlocal res
        if remain == 0:
            res.append(path) 
            return
        
        for c in candidates:
            if (path[-1] if path else 0) <= c <= remain:
                backtrack(remain - c, path + [c])
    
    backtrack(target, [])
    return res

print(combinationSum([2, 3, 5], 8))