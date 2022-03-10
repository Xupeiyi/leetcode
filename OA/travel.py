from bisect import bisect_left

def wait(departures, t):
    idx = bisect_left(departures, t)
    return departures[idx]


def travel(a2b, b2a, trips):
    curr_t = 0
    for _ in range(trips):
        curr_t = wait(a2b, curr_t)
        curr_t += 100
        curr_t = wait(b2a, curr_t)
        curr_t += 100
    return curr_t


if __name__ == '__main__':
    a2b = [109, 200, 500]
    b2a = [99, 210, 600]
    print(wait(a2b, 0) == 109)
    print(wait(a2b, 100) == 109)
    print(wait(a2b, 109) == 109)
    print(wait(a2b, 110) == 200)
    
    ans = travel(a2b ,b2a, 2)
    print(ans)

    ans = travel([0, 200, 500], [99, 210, 600], 1)
    print(ans)