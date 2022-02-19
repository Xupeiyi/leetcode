
def constructDistancedSequence(n: int):
    if n == 1:
        return [1]

    res = None
    def backtrack(status, idx, optional):
        nonlocal res
        if res != None:
            return

        # 若所有空白都已填上
        if idx == 2*n -1:
            res = status
            return 
        
        # 若当前位置无数字
        if status[idx] == 0:
            for i in optional:
                if i == 1:
                    status2 = status.copy()
                    status2[idx] = i

                    optional2 = optional.copy()
                    optional2.remove(i)
                    
                    backtrack(status2, idx + 1, optional2)

                # 若其后偏移i的位置上也没有（且不超出列表长度）
                elif idx + i <= 2*n - 2 and status[idx + i] == 0: 
                    status2 = status.copy()
                    status2[idx] = i
                    status2[idx + i] = i
                    
                    optional2 = optional.copy()
                    optional2.remove(i)
                    
                    backtrack(status2, idx + 1, optional2)
        # 若当前位置已有数字，则继续
        else:
            backtrack(status, idx + 1, optional)
            
    
    status = [0] * (2*n -1)
    status[0] = n
    status[n] = n
    init_optional = list(range(n - 1, 0, -1))
    
    backtrack(status, 1, init_optional)

    return res



print(constructDistancedSequence(5))
