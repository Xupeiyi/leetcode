def minOperations(logs: list) -> int:
    stack = []
    while(logs):
        directory = logs.pop(0)
        if directory == '../':
            if stack != []:
                stack.pop(-1)
        elif directory == './':
            continue
        else:
            stack.append(directory)
    
    return len(stack)    

if __name__ == '__main__':
    logs = ["d1/","d2/","../","d21/","./"]
    print(minOperations(logs))