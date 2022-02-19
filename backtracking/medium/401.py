def readBinaryWatch(num: int):
    def parse_time(path: str) -> str:
        hours = int(path[: 4].ljust(4, "0"), 2) 
        minutes = int(path[4:].ljust(6, "0"), 2)
        return hours, minutes

    def is_legal(path: str) -> bool:
        hours, minutes = parse_time(path)
        if hours > 11 or minutes > 59:
            return False
        return True

    def traceback(num, path):
        """
        num: 还要点亮几盏灯
        current: 当前选择点亮哪盏灯
        path: 当前选择的路径
        """
        if num == 0:
            hours, minutes = parse_time(path)
            res.append("%d:%02d" %(hours, minutes))
            return
        
        for idx in range(len(path), 10):
            # 如果点亮这盏灯
            remain = 10 - idx # 包含这盏灯在内，最多还能点亮几盏
            
            # 如果还有足够多的灯可以点亮，且这盏灯可以合法点亮
            if remain >= num  and is_legal(path + "1"): # 
                traceback(num - 1, path + "1")
            
            # 如果不点亮这盏灯, 则继续
            path = path + "0"
    
    res = []
    traceback(num, "")
    return res

def readBinaryWatch2(num: int):
    def parse_time(lights) -> str:
        hours = sum((x*y for x, y in zip([8, 4, 2, 1], lights[:4]))) 
        minutes = sum((x*y for x, y in zip([32, 16, 8, 4, 2, 1], lights[4:]))) 
        return hours, minutes

    def get_hours(lights):
        hours = sum((x*y for x, y in zip([8, 4, 2, 1], lights[:4]))) 
        return hours
    
    def get_minutes(lights):
        minutes = sum((x*y for x, y in zip([32, 16, 8, 4, 2, 1], lights[4:]))) 
        return minutes

    def is_legal(lights, i) -> bool:
        if i <= 3:
            hours = get_hours(lights)
            if hours > 11:
                return False
        else:
            minutes = get_minutes(lights)
            if minutes > 59:
                return False
        return True

    def traceback(lights, idx, num):
        """
        num: 还要点亮几盏灯
        current: 当前选择点亮哪盏灯
        path: 当前选择的路径
        """
        if num == 0:
            hours, minutes = parse_time(lights)
            res.append("%d:%02d" %(hours, minutes))
            return
        
        for i in range(idx, 10):
            # 如果点亮这盏灯
            remain = 10 - i # 包含这盏灯在内，最多还能点亮几盏
            
            # 如果还有足够多的灯可以点亮，且这盏灯可以合法点亮
            lights[i] = 1
            if remain >= num  and is_legal(lights, i): # 
                traceback(lights, i + 1, num - 1)
            
            # 如果不点亮这盏灯, 则继续
            lights[i] = 0
    
    res = []
    traceback([0] * 10, 0, num)
    return res


if __name__ == '__main__':
    import time
    print(set(readBinaryWatch(3)) == set(readBinaryWatch2(3)))
    t1 = time.time()
    readBinaryWatch(3)
    print((time.time() - t1) * 100000000)

    t1 = time.time()
    readBinaryWatch2(3)
    print((time.time() - t1) * 100000000)