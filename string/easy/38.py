def describe(number: str) -> str:
    result = ''
    number += '/' # 添加哨兵，方便判断边界

    count = 1
    previous = number[0] # 前一个数字字符
    for char in number[1:]:
        if char == previous:
            count += 1
        else:
            result += str(count)
            result += str(previous)
            count = 1
            previous = char

    return result

def countAndSay(n):
    result = '1'
    for i in range(2, n + 1):
        result = describe(result)
    
    return result

print(describe('312211'))
print(countAndSay(2))