# original
from collections import Counter

def firstUniqueChar0(s):
    s_count = Counter(s)
    # for i, char in enumerate(s_count.keys()): # 其实这样是错的。s_count无法保证键按原顺序排列。
    for i, char in enumerate(s): 
        if s_count[char] == 1:
            return i
    return -1

# 上面的算法要遍历s两次。

# 下面是leetcode官方答案。
def firstUniqueChar1(s):
    position = dict() # key: 字符, value: 字符出现在s中的位置，如果再次出现则置为-1
    for i, char in enumerate(s):
        if char in position:
            position[char] = -1
        else:
            position[char] = i
    
    # 遍历position, 寻找中最小值
    first = n = len(s)
    for pos in position.values():
        if pos != -1 and pos < first:
            first = pos
    if first == n:
        first = -1
    return first

# 维护一个队列，保证队首总是只出现过一次的字符。
# 这样不用再遍历position一次。
from collections import deque

def firstUniqueChar2(s):
    position = dict()
    queue = deque()
    first = n = len(s)

    for i, char in enumerate(s):
        if char not in position:
            position[char] = i
            queue.append(char)
        else:
            position[char] = -1
            while(queue and position[queue[0]] == -1):
                queue.popleft()
    return -1 if not queue else position[queue[0]]

print(firstUniqueChar2("leetcodel"))

