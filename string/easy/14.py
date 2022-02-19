def longestCommonPrefix(strs: list) -> str:
    if strs == []:
        return ""

    common_prefix = ""
    for i, letters in enumerate(zip(*strs)):
        if len(set(letters)) == 1:
            common_prefix += letters[0]
        else:
            break
    
    return common_prefix


strs0 = ["flower", "flow", "flight"]
strs1 = ["fat", "forest", "funk"]
strs2 = ["expensive", "expenditure", "expendicular"]
strs3 = ["dog","racecar","car"]
strs4 = []
strs5 = ["dog", "dog", "dog"]
strs6 = ["ab", "a"]
print(longestCommonPrefix(strs0) == "fl")
print(longestCommonPrefix(strs1) == "f")
print(longestCommonPrefix(strs2) == "expen")
print(longestCommonPrefix(strs3) == "")
print(longestCommonPrefix(strs4) == "")
print(longestCommonPrefix(strs5) == "dog")
print(longestCommonPrefix(strs6) == "a")