def countVowelStrings(n):
    table = [[1, 1, 1, 1, 1]] +[[0, 0, 0, 0, 1]] * (n - 1)
    for row in range(1, n):
        for col in range(3, -1, -1):
            table[row][col] = table[row][col + 1] + table[row - 1][col]
    return sum(table[n - 1])

import time
t1 = time.time()
print(countVowelStrings(50))
print(time.time() - t1)