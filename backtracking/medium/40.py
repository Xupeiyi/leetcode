from collections import Counter

def combinationSum2(candidates:list, target):
    count_candidates = Counter(candidates)
    candidates = [(c, count) for c, count in count_candidates.items()]
    candidates.sort()
    res = []

    def backtrack(s, idx, path):
        if s == target:
            ans = []
            for c, n in path:
                ans += [c] * n
            res.append(ans)
            return         

        if idx >= len(candidates):
            return

        candidate = candidates[idx][0]
        num = candidates[idx][1]
        for n in range(0, num + 1):
            if s + n * candidate <= target:
                backtrack(s + n * candidate, idx + 1, path + [(candidate, n)])
            else:
                break
    
    backtrack(0, 0, [])
    return res


print(combinationSum2([10, 1, 2, 7, 6, 1 ,5], 8))
print(combinationSum2([2, 5, 2, 1, 2], 5))