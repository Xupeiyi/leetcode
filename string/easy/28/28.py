def strStr(haystack: str, needle: str) -> int:
    """
    给定一个 haystack 字符串和一个 needle 字符串，
    在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
    如果不存在，则返回-1。
    """
    if needle == "":
        return 0

    len_needle = len(needle)
    len_haystack = len(haystack)
    # 构建移动窗口
    for i in range(len_haystack - len_needle + 1):
        if needle == haystack[i: i + len_needle]:
            return i
    return -1

print(strStr("hello", "ll"))
print(strStr("aaaaaa", "bba"))