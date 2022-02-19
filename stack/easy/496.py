def nextGreaterElement(nums1, nums2) -> list:
    stack = [] # 从栈底到栈顶不严格单调递增
    greater_right = {}

    for n2 in nums2:
        while (stack != [] and n2 > stack[-1]):
            e = stack.pop()
            greater_right[e] = n2
        stack.append(n2)
    
    ans = [greater_right.get(n1, -1) for n1 in nums1]
    return ans

n1 = [2, 4]
n2 = [1, 2, 3, 4]
print(nextGreaterElement(n1, n2))