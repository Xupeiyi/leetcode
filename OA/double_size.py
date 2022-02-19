def doubleSize(arr, num):
    for n in sorted(arr):
        if n == num:
            num *= 2
    return num