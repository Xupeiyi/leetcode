def valid(ip_string):
    if not ip_string:
        return False
    
    if len(ip_string) > 1 and ip_string[0] == "0":
        return False
    
    if int(ip_string) > 255:
        return False
    
    return True
    

class Solution:
    def restoreIpAddresses(self, s: str):
        ans = []
        if not s:
            return ans
        
        def backtrack(ip_string, usable, path):
            nonlocal ans
            if usable == 0:
                if valid(ip_string):
                    ans.append(path+ip_string)
                return
            
            for address, rest in {(ip_string[:1], ip_string[1:]),
                                  (ip_string[:2], ip_string[2:]),
                                  (ip_string[:3], ip_string[3:])}:
                if valid(address):
                    backtrack(rest, usable-1, path+address+".")
        
        backtrack(s, 3, "")
        return ans
                    

if __name__ == '__main__':
    s = Solution()
    ans = s.restoreIpAddresses("25525511135")
    print(ans)