class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        curr1, curr2 = 0, 0
        n1, n2 = len(version1), len(version2)

        while curr1 < n1 or curr2 < n2:
            i = curr1
            while i < n1 and version1[i] != '.':
                i += 1
            if curr1 < n1:
                num1 = int(version1[curr1:i]) 
                curr1 = i + 1 
            else:
                num1 = 0

            i = curr2
            while i < n2 and version2[i] != '.':
                i += 1
            if curr2 < n2:
                num2 = int(version2[curr2:i]) 
                curr2 = i + 1 
            else:
                num2 = 0

            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0
        
if __name__ == '__main__':
    s = Solution()
    ans = s.compareVersion('1.10', '1.10.01')
    print(ans)