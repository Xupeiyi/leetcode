
class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        diff = dict()
        for i in range(len(s)):
            if s[i] not in diff:
                # 其实这样不太高效，因为dict.values() 不像dict.keys(), 它不是 set-like的
                # 更高效的做法是再建立一个 t[i]->s[i]的字典， 维护双射关系
                if t[i] not in diff.values():  
                    diff[s[i]] = t[i]
                else:
                    return False
            else:
                if diff[s[i]] != t[i]:
                    return False
        return True


# 秀儿快坐下
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


if __name__ == '__main__':
    s = Solution()
    ans = s.isIsomorphic("paper", "title")
    print(ans)