def next_one(input_str, start, k):
    """find the k-th 1 after start"""
    if k == 0:
        return start
    
    n = len(input_str)
    end = start + 1
    n_ones = 0
    while end < n and n_ones < k:
        if input_str[end] == '1':
            n_ones += 1
            
            if n_ones == k:
                return end
        
        end += 1
        
    return -1
    
    
def str_cmp(str1, str2):
    if len(str1) < len(str2):
        return str1
    elif len(str1) > len(str2):
        return str2
    else:
        return min(str1, str2)
    

def k_smallest_substring(input_str, k):
    if k == 1:
        return "1"
    
    i = next_one(input_str, -1, 1)
    
    j = next_one(input_str, i, k-1)
    ans = input_str[i:j+1]
    
    while i < len(input_str):
        i = next_one(input_str, i, 1)
        j = next_one(input_str, j, 1)
        
        # if there is no more 1 after j
        if j == -1:
            break
        
        ans = str_cmp(ans, input_str[i:j+1])
        
    return ans
    
    
if __name__ == '__main__':
    # print(next_one("11011", 0, 2))
    print(k_smallest_substring("11011", 1))
    # print(k_smallest_substring("1110111", 3) == "111")
    # print(k_smallest_substring("110011101", 4) == "100111")
    #
    # print(k_smallest_substring("10100001001010101", 5) == "1000010010101")
    #
    # print(k_smallest_substring("110011101", 4))
    # print(k_smallest_substring("10100001001010101", 5))