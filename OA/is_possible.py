def is_possible(a, b, c, d):
    ans = "No"
    
    def backtrack(x, y):
        nonlocal ans
        if (x, y) == (c, d):
            ans = "Yes"
            return
        
        for new_x, new_y in [(x, x + y), (x + y, y)]:
            if new_x <= c and new_y <= d:
                backtrack(new_x, new_y)
    
    backtrack(a, b)
    return ans


def solution():
    a = input()
    b = input()
    c = input()
    d = input()
    return is_possible(int(a), int(b), int(c), int(d))


if __name__ == '__main__':
    # ans = solution()
    # print(ans)
    ans = is_possible1(1, 4, 5, 9)
    # ans = is_possible(35, 13, 455955547, 420098884)

    print(ans)
