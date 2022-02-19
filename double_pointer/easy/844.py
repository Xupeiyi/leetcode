def find_valid_idx(string, idx, skip):
    if idx == -1 or (string[idx] != '#' and skip == 0):
        return idx

    skip = skip + 1 if string[idx] == '#' else skip - 1
    return find_valid_idx(string, idx-1, skip)


def find_valid_idx1(string, idx):
    skip = 0
    while not (idx == -1 or (string[idx] != '#' and skip == 0)):
        skip = skip + 1 if string[idx] == '#' else skip - 1
        idx -= 1
    
    return idx
    

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        length_s, length_t = len(S), len(T)

        i_s, i_t = length_s, length_t

        while True:
            
            # find the next valid char in s
            i_s = find_valid_idx1(s, i_s-1)
            i_t = find_valid_idx1(t, i_t-1)

            if i_s >= 0 and i_t >= 0:
                if S[i_s] != T[i_t]:
                    return False
            else:
                break

        if (i_s * i_t <= 0):
            return False

        return True


if __name__ == '__main__':
    sol = Solution()
    s = "ac#d#e#f#"
    t = "ad#"
    print(sol.backspaceCompare(s, t))
