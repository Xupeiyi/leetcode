def hanota(A: List[int], B: List[int], C: List[int]) -> None:
    """
    Do not return anything, modify C in-place instead.
    """
    n = len(A)
    move(n, A, B, C)

def move(n, A, B, C):
    if n == 1:
        C.append(A.pop())
    else:
        move(n-1, A, C, B)
        C.append(A.pop())
        move(n-1, B, A, C)