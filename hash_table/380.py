import random


class RandomizedSet:

    def __init__(self):
        self.pos = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        size = len(self.data)
        self.pos[val] = size
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        val_idx = self.pos[val]
        tail_idx = len(self.data) - 1
        tail_val = self.data[tail_idx]
        self.data[tail_idx], self.data[val_idx] = self.data[val_idx], self.data[tail_idx] 
        self.pos[tail_val], self.pos[val] = val_idx, tail_idx

        self.data.pop(-1)
        self.pos.pop(val)
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.data)-1)
        return self.data[idx]
