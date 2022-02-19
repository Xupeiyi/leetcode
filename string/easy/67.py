# original
def adder(x, y, z):
    s = x ^ y ^ z
    c = (x & y) | (x & z) | (y & z) 
    return s, c

def addBinary(a:str, b:str) -> str:
    d = len(b) - len(a)
    a = '0' * d + a # 若 d <= 0 , 则 '0' * d = ''
    b = '0' * (-d) + b

    sum_bits = ''
    carry = 0
    for a_bit, b_bit in zip(a[::-1], b[::-1]):
        s, carry = adder(int(a_bit), int(b_bit), carry)
        sum_bits = str(s) + sum_bits
    if carry:
        sum_bits = '1' + sum_bits

    return sum_bits

print(addBinary("0", "0"))
print(addBinary("1", "11"))
print(addBinary("1010", "1011"))


print(adder(0, 0, 0))
print(adder(0, 0, 1))
print(adder(0, 1, 0))
print(adder(0, 1, 1))
print(adder(1, 0, 0))
print(adder(1, 0, 1))
print(adder(1, 1, 0))
print(adder(1, 1, 1))

# 更简洁，也更快的方法。利用位运算。
def addBinary2(a, b):
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y # 无进位相加结果
        carry = (x & y) << 1 # 进位
        x, y = answer, carry
    return bin(x)[2:] # 前两位为'0b'

