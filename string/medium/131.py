from functools import lru_cache

@lru_cache()
def is_panlindrome(string: str) -> bool:
    i, j = 0, len(string) - 1
    
    while (i < j):
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    
    return True

def partition(s: str) -> list:
    """使用回溯算法"""
    
    def backtrack(remain, path):
        nonlocal res
        
        # 终止条件
        if not remain:
            res.append(path)
            return
        
        # 本层树的每个节点
        for i in range(len(remain)):
            cut = remain[: i+1]
            if is_panlindrome(cut):
                backtrack(remain[i+1:], path + [cut])
    
    res = []
    backtrack(s, [])
    return res

print(partition("aab"))
print(partition("xyzyxaab"))